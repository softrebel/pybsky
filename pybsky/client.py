import requests
from .mixins import LoginMixin, FeedMixin, GraphMixin, ProfileMixin, ServerMixin
from .core import (
    USER_AGENTS,
    SERVER_URL,
    CREATE_RECORD_URL,
    BSKY_BASE_URL,
    DELETE_RECORD_URL,
)
import random


class Client(LoginMixin, FeedMixin, GraphMixin, ProfileMixin, ServerMixin):
    server: str = None
    proxies: str = None
    access_jwt: str = None
    refresh_jwt: str = None
    user_agent: str = None
    session: requests.Session = None
    own_profile: dict = None

    def __init__(self, proxies=None, server=None, **kwargs):
        super().__init__(**kwargs)

        self.server = server if server else SERVER_URL
        self.session = requests.Session()
        self.session.timeout = 20
        self.user_agent = random.choice(USER_AGENTS)

        self.proxies = None
        if proxies:
            self.proxies = proxies
            self.session.proxies = proxies

        headers = {
            "origin": "https://bsky.app",
            "referer": "https://bsky.app/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": self.user_agent,
        }
        self.session.headers.update(headers)

    @property
    def did(self):
        if not self.own_profile or "did" not in self.own_profile.keys():
            return None
        return self.own_profile["did"]

    @property
    def handle(self):
        if not self.own_profile or "handle" not in self.own_profile.keys():
            return None
        return self.own_profile["handle"]

    def get_actor(self, username: str) -> str:
        return username
        # if 'did' in username:
        #     return username
        # if self.server in username:
        #     return username
        # else:
        #     return f"{username}.{self.server}"

    def send_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
        json: dict = None,
    ):
        self.session.headers.update({"Authorization": f"Bearer {self.access_jwt}"})
        if headers:
            self.session.headers.update(headers)

        response = self.session.request(
            method=method, url=url, params=params, data=data, json=json
        )
        return response

    def create_record(self, collection: str, record: dict, repo: str):
        url = f"{BSKY_BASE_URL}{CREATE_RECORD_URL}"
        data = dict(collection=collection, record=record, repo=repo)
        return self.send_request(method="POST", url=url, json=data)

    def delete_record(self, collection: str, repo: str, rkey: str):
        url = f"{BSKY_BASE_URL}{DELETE_RECORD_URL}"
        data = dict(collection=collection, repo=repo, rkey=rkey)
        return self.send_request(method="POST", url=url, json=data)
