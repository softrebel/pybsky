
import requests
from mixins import LoginMixin, FeedMixin
from core import USER_AGENTS, SERVER_URL
import random
from pydantic import BaseModel


class Client(BaseModel, LoginMixin, FeedMixin):
    server: str = None
    proxies: str = None
    access_jwt: str = None
    refresh_jwt: str = None
    user_agent: str = None
    session: requests.session = None

    def __init__(
        self,
        proxies=None,
        server=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.server = server if server else SERVER_URL
        self.session = requests.Session()
        self.session.timeout = 20
        self.user_agent = random.choice(USER_AGENTS)

        self.proxies = None
        if proxies:
            self.proxies = proxies
            self.session.proxies = proxies

    def get_actor(self, username: str) -> str:
        if self.server in username:
            return username
        else:
            return f'{username}.{self.server}'
