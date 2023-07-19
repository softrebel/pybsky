

from core.exceptions import AuthenticationRequired, UnknownResponse
from core.utils import validate_value

class FeedMixin():

    def get_author_feed(self, actor: str, limit: int = 30):
        validate_value(actor,str)
        headers = {
            'origin': 'https://bsky.app',
            'referer': 'https://bsky.app/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': self.user_agent,
        }

        params = {
            'actor': self.get_actor(actor),
            'limit': limit,
        }
        url = 'https://bsky.social/xrpc/com.atproto.server.createSession'
        response = self.session.get(url,params=params, headers=headers)

        if response.status_code == 200:
            self.access_jwt = response.json()["accessJwt"]
            self.refresh_jwt = response.json()["refreshJwt"]
            return True
        elif response.status_code == 401:
            raise AuthenticationRequired(
                "Invalid identifier(username.bsky.social) or password")
        else:
            raise UnknownResponse(
                f"status code => {response.status_code} , response => {response.text}")
        # TODO => handle all type of response
