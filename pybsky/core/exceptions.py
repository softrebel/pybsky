class AuthenticationRequiredException(Exception):
    """Invalid identifier(username.bsky.social) or password"""


class UnknownResponseException(Exception):
    """Unknown Response"""


class BadRequestResponseException(Exception):
    """Bad Response"""
