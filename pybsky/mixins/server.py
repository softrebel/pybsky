from ..core import validate_get_response, GET_ACCOUNT_INVITATION_URL, BSKY_BASE_URL


class ServerMixin:
    def get_account_invitation(self):
        url = f"{BSKY_BASE_URL}{GET_ACCOUNT_INVITATION_URL}"
        response = self.send_request(method="GET", url=url)
        validated_response = validate_get_response(response)
        return validated_response
