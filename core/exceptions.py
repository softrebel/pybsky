class AuthenticationRequired(Exception):
    """Invalid identifier(username.bsky.social) or password"""

class UnknownResponse(Exception):
    """Unknown Response"""