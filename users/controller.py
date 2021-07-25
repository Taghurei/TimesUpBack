from flask_login import login_user, logout_user

from users.exceptions import IncorrectCredentialsException
from users.manager import UserManager
from users.model import User


def login(inputs):
    user = UserManager().get_one_by_query(inputs)
    if not user:
        raise IncorrectCredentialsException(error_code=42)
    else:
        login_user(user)
        return user


def signup(inputs):
    inputs["permissions"] = []
    user = User(**inputs)
    print("e")
    if UserManager().insert_one(user):
        login_user(user)
        return user


def logout():
    logout_user()