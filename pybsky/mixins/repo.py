from ..core import (
    validate_get_response,
    BSKY_BASE_URL,
    UPLOAD_BLOB_URL,
    LIKE_URL,
)


class RepoMixin:
    def upload_blob(self, file: bytes):
        url = f"{BSKY_BASE_URL}{UPLOAD_BLOB_URL}"
        data = file
        headers = {"content-type": "image/jpeg"}
        response = self.send_request(method="POST", url=url, data=data, headers=headers)
        validated_response = validate_get_response(response)
        return validated_response

    def like(self, uri: str, cid: str):
        createdAt = self.get_createdAt_now()
        record = {
            "createdAt": createdAt,
            "$type": LIKE_URL,
            "subject": {"uri": uri, "cid": cid},
        }

        response = self.create_record(collection=LIKE_URL, repo=self.did, record=record)
        validated_response = validate_get_response(response)
        return validated_response
