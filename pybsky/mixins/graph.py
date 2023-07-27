from ..core import (
    validate_get_response,
    validate_value,
    GET_Followers_URL,
    GET_FOLLOWS_URL,
    BSKY_BASE_URL,
    ProfileRequiredException,
    FollOW_URL,
    NotFollowingException,
)
from datetime import datetime, timezone


class GraphMixin:
    def get_followers(self, actor: str, limit: int = 30, cursor: str = None):
        validate_value(actor, str)
        validate_value(limit, int)
        if cursor:
            validate_value(cursor, str)
        params = {
            "actor": self.get_actor(actor),
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        url = f"{BSKY_BASE_URL}{GET_Followers_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response

    def get_followings(self, actor: str, limit: int = 30, cursor: str = None):
        validate_value(actor, str)
        validate_value(limit, int)
        if cursor:
            validate_value(cursor, str)
        params = {
            "actor": self.get_actor(actor),
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        url = f"{BSKY_BASE_URL}{GET_FOLLOWS_URL}"
        response = self.send_request(method="GET", url=url, params=params)
        validated_response = validate_get_response(response)
        return validated_response

    def follow(self, actor: str):
        exact_actor = self.get_actor(actor)
        if not self.did:
            raise ProfileRequiredException()
        if "did" not in exact_actor:
            actor_profile = self.get_profile(exact_actor)
            subject = actor_profile["did"]
        else:
            subject = exact_actor
        now = datetime.now(timezone.utc)
        createdAt = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        record = {"subject": subject, "createdAt": createdAt, "$type": FollOW_URL}

        response = self.create_record(
            collection=FollOW_URL, repo=self.did, record=record
        )
        validated_response = validate_get_response(response)
        return validated_response

    def unfollow_by_actor(self, actor: str):
        exact_actor = self.get_actor(actor)
        if not self.did:
            raise ProfileRequiredException()
        profile = self.get_profile(exact_actor)
        if "viewer" not in profile or "following" not in profile["viewer"]:
            raise NotFollowingException()
        following_record = profile["viewer"]["following"]
        rkey = following_record.split("/")[-1]
        return self.unfollow_by_rkey(rkey)

    def unfollow_by_rkey(self, rkey: str):
        response = self.delete_record(collection=FollOW_URL, repo=self.did, rkey=rkey)
        validated_response = validate_get_response(response)
        return validated_response
