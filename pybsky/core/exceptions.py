class AuthenticationRequiredException(Exception):
    """Invalid identifier(username.bsky.social) or password"""


class UnknownResponseException(Exception):
    """Unknown Response"""


class BadRequestResponseException(Exception):
    """Bad Response"""


class ProfileRequiredException(Exception):
    """Profile required Exception"""


class NotFollowingException(Exception):
    """Not Following Exception"""
