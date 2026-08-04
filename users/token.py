from flask import current_app
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

TOKEN_SALT = "timesup-auth"
# A month: long enough to keep a phone logged in between two game nights
TOKEN_MAX_AGE = 60 * 60 * 24 * 30


def serializer():
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=TOKEN_SALT)


def generate_token(user):
    return serializer().dumps(user.user_id)


def read_token(token: str):
    """Return the user_id carried by the token, or None if it is invalid or expired."""
    try:
        return serializer().loads(token, max_age=TOKEN_MAX_AGE)
    except (BadSignature, SignatureExpired):
        return None
