from ..core import (
    validate_get_response,
    validate_value,
    BSKY_BASE_URL,
    LIST_NOTIFICATION_URL,
    NOTIFICATION_UPDATE_SEEN_URL,
)


class NotificationMixin:
    def get_list_notifications(self, limit: int = 30, cursor: str = None):
        validate_value(limit, int)
        if cursor:
            validate_value(cursor, str)
        params = {
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        url = f"{BSKY_BASE_URL}{LIST_NOTIFICATION_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response

    def update_seen(self, seen_at: str = None):
        if seen_at:
            validate_value(seen_at, str)
        else:
            seen_at = self.get_createdAt_now()
        data = {
            "seenAt": seen_at,
        }
        url = f"{BSKY_BASE_URL}{NOTIFICATION_UPDATE_SEEN_URL}"
        response = self.send_request(method="POST", url=url, json=data)
        validated_response = validate_get_response(response)
        return validated_response
