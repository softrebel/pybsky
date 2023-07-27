from ..core import validate_get_response, validate_value, GET_PROFILE_URL, BSKY_BASE_URL


class ProfileMixin:
    def get_profile(self, actor: str):
        validate_value(actor, str)
        params = {
            "actor": self.get_actor(actor),
        }
        url = f"{BSKY_BASE_URL}{GET_PROFILE_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response
