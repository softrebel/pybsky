import random
import requests

from ..core import USER_AGENTS, validate_value, validate_get_response


class LoginMixin:
    def login(self, username: str, password: str):
        validate_value(username, str)
        validate_value(password, str)
        if len(username) == 0:
            raise ValueError("username should not be empty")
        if len(password) == 0:
            raise ValueError("username should not be empty")

        session = requests.Session()
        session.timeout = 30
        session.proxies = self.session.proxies

        self.user_agent = random.choice(USER_AGENTS)

        headers = {
            "origin": "https://bsky.app",
            "referer": "https://bsky.app/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": self.user_agent,
        }

        payload = {
            "identifier": self.get_actor(username),
            "password": password,
        }
        url = "https://bsky.social/xrpc/com.atproto.server.createSession"
        response = requests.post(url, headers=headers, json=payload)

        validated_response = validate_get_response(response)
        self.access_jwt = validated_response["accessJwt"]
        self.refresh_jwt = validated_response["refreshJwt"]
        return validated_response
