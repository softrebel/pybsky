import json
import random
import requests

from core import USER_AGENTS,validate_value
from core.exceptions import AuthenticationRequired, UnknownResponse


class LoginMixin():

    def login(self, username: str, password: str):
        validate_value(username,str)
        validate_value(password,str)
        if len(username) == 0:
            raise ValueError('username should not be empty')
        if len(password) == 0:
            raise ValueError('username should not be empty')


        session = requests.Session()
        session.timeout = 30
        session.proxies = self.session.proxies

        self.user_agent = random.choice(USER_AGENTS)

        headers = {
            'origin': 'https://bsky.app',
            'referer': 'https://bsky.app/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': self.user_agent,
        }

        payload = {
            'identifier': self.get_actor(username),
            'password': password,
        }
        url = 'https://bsky.social/xrpc/com.atproto.server.createSession'
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            self.access_jwt = response.json()["accessJwt"]
            self.refresh_jwt = response.json()["refreshJwt"]
            return True
        elif response.status_code == 401:
            content = json.loads(response.text)
            raise AuthenticationRequired(content['message'])
        else:
            raise UnknownResponse(
                f"status code => {response.status_code} , response => {response.text}")
        # TODO => handle all type of response
