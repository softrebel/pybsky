
import random
import requests

from ..configs import USER_AGENTS
from ..configs.exceptions import AuthenticationRequired , UnknownResponse


class LoginMixin():

    def login(self , username:str , password:str):

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
            'identifier': f'{username}.bsky.social',
            'password': password,
        }
        url = 'https://bsky.social/xrpc/com.atproto.server.createSession'
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200 :
            self.access_jwt = response.json()["accessJwt"]
            self.refresh_jwt = response.json()["refreshJwt"]
            return True
        elif response.status_code == 401 :
            raise AuthenticationRequired("Invalid identifier(username.bsky.social) or password")
        else:
            raise UnknownResponse(f"status code => {response.status_code} , response => {response.text}")
        #TODO => handle all type of response




        