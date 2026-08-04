from werkzeug.security import check_password_hash, generate_password_hash

from users.exceptions import (
    TimesUpNicknameTakenException,
    TimesUpWeakPasswordException,
    TimesUpWrongCredentialsException,
)
from users.manager import UserManager
from users.model import User
from users.token import generate_token, read_token

MINIMUM_PASSWORD_LENGTH = 4


def register_user(nickname: str, password: str):
    """Create a user and return it with a fresh token."""
    if not isinstance(password, str) or len(password) < MINIMUM_PASSWORD_LENGTH:
        raise TimesUpWeakPasswordException(minimum_length=MINIMUM_PASSWORD_LENGTH)

    user_manager = UserManager()
    clean_nickname = clean(nickname)
    if user_manager.get_by_nickname(clean_nickname):
        raise TimesUpNicknameTakenException()

    user = User(
        nickname=clean_nickname, password_hash=generate_password_hash(password),
    )
    user_manager.insert_one(user)
    return user, generate_token(user)


def login_user(nickname: str, password: str):
    user = UserManager().get_by_nickname(clean(nickname))
    if not user or not check_password_hash(user.password_hash, password or ""):
        raise TimesUpWrongCredentialsException()
    return user, generate_token(user)


def get_user_from_token(token: str):
    """Return the user behind a token, or None: logging in stays optional."""
    if not token:
        return None
    user_id = read_token(token)
    if not user_id:
        return None
    return UserManager().get(user_id)


def clean(nickname: str):
    return nickname.strip() if isinstance(nickname, str) else nickname
