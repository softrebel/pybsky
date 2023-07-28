from ..core import (
    validate_get_response,
    IMAGES_URL,
    POST_URL,
)


class PostMixin:
    def post_text(
        self,
        text: str,
        langs: list = None,
    ):
        if not langs or len(langs) == 0:
            langs = ["fa", "en"]
        createdAt = self.get_createdAt_now()
        record = {
            "text": text,
            "langs": langs,
            "createdAt": createdAt,
            "$type": POST_URL,
        }
        response = self.create_record(collection=POST_URL, repo=self.did, record=record)
        validated_response = validate_get_response(response)
        return validated_response

    def reply_text(
        self,
        text: str,
        root_cid: str,
        root_uri: str,
        parent_cid: str,
        parent_uri: str,
        langs: list = None,
    ):
        if not langs or len(langs) == 0:
            langs = ["fa", "en"]
        createdAt = self.get_createdAt_now()
        record = {
            "text": text,
            "langs": langs,
            "createdAt": createdAt,
            "$type": POST_URL,
            "reply": {
                "root": {"cid": root_cid, "uri": root_uri},
                "parent": {"cid": parent_cid, "uri": parent_uri},
            },
        }

        response = self.create_record(collection=POST_URL, repo=self.did, record=record)
        validated_response = validate_get_response(response)
        return validated_response

    def post_text_images(self, text: str, images: list, langs: list = None):
        if not langs or len(langs) == 0:
            langs = ["fa", "en"]
        createdAt = self.get_createdAt_now()
        record = {
            "text": text,
            "langs": langs,
            "createdAt": createdAt,
            "$type": POST_URL,
            "embed": {
                "$type": IMAGES_URL,
                "images": [{"image": x, "alt": ""} for x in images],
            },
        }

        response = self.create_record(collection=POST_URL, repo=self.did, record=record)
        validated_response = validate_get_response(response)
        return validated_response
