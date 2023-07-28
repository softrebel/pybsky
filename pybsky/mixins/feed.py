from ..core import (
    validate_get_response,
    validate_value,
    FEED_URL,
    BSKY_BASE_URL,
    GET_TIMELINE_URL,
    GET_POSTS_URL,
    GET_POST_THREAD,
)


class FeedMixin:
    def get_author_feed(self, actor: str, limit: int = 30):
        validate_value(actor, str)
        headers = {
            "origin": "https://bsky.app",
            "referer": "https://bsky.app/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": self.user_agent,
            "authorization": f"Bearer {self.access_jwt}",
        }

        params = {
            "actor": self.get_actor(actor),
            "limit": limit,
        }
        url = f"{BSKY_BASE_URL}{FEED_URL}"
        response = self.session.get(url, params=params, headers=headers)
        validated_response = validate_get_response(response)
        return validated_response

    def get_timeline(self, algorithm: str = "reverse-chronological", limit: int = 30):
        validate_value(algorithm, str)
        validate_value(limit, int)
        params = {
            "actor": algorithm,
            "limit": limit,
        }
        url = f"{BSKY_BASE_URL}{GET_TIMELINE_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response

    def get_posts(self, uris: str):
        validate_value(uris, str)
        params = {
            "uris": uris,
        }
        url = f"{BSKY_BASE_URL}{GET_POSTS_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response

    def get_post_thread(self, uri: str):
        validate_value(uri, str)
        params = {
            "uri": uri,
        }
        url = f"{BSKY_BASE_URL}{GET_POST_THREAD}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response
