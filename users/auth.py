from functools import wraps

from flask import g, request

from users.controller import get_user_from_token
from users.exceptions import TimesUpNotLoggedInException

BEARER_PREFIX = "Bearer "


def get_current_user():
    """Return the logged in user, or None when the request comes from a guest."""
    header = request.headers.get("Authorization", "")
    token = header[len(BEARER_PREFIX) :] if header.startswith(BEARER_PREFIX) else header
    return get_user_from_token(token.strip())


def login_required(route):
    """Reject guests, and expose the caller as g.current_user."""

    @wraps(route)
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user:
            raise TimesUpNotLoggedInException()
        g.current_user = user
        return route(*args, **kwargs)

    return wrapper
