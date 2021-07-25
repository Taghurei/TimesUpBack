import time
from uuid import uuid4
from flask_login import UserMixin

from core.model import Document
from core.exceptions import TimesUpEmptyFieldException, TimesUpTypeException


class User(Document, UserMixin):
    fields = [
        "_id",
        "username",
        "password",
        "email",
        "firstname",
        "lastname",
        "is_active",
        "created_at",
        "permissions",
    ]

    export_fields = [
        "user_id",
        "username",
        "email",
        "firstname",
        "lastname",
        "is_active",
        "created_at",
        "permissions",
    ]

    editable_fields = ["email", "firstname", "lastname"]

    def __init__(
        self,
        username: str = "",
        password: str = "",
        email: str = "",
        firstname: str = "",
        lastname: str = "",
        is_active: bool = True,
        permissions: list = [],
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.user_id = self._id
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.permissions = permissions
        self.verify()

    def verify(self):
        if not isinstance(self.username, str):
            raise TimesUpTypeException(error_code=35, incorrect_input="username")
        if not isinstance(self.password, str):
            raise TimesUpTypeException(error_code=36, incorrect_input="password")
        if not isinstance(self.email, str):
            raise TimesUpTypeException(error_code=37, incorrect_input="email")
        if not isinstance(self.firstname, str):
            raise TimesUpTypeException(error_code=38, incorrect_input="firstname")
        if not isinstance(self.lastname, str):
            raise TimesUpTypeException(error_code=30, incorrect_input="lastname")
        if not isinstance(self.permissions, list):
            raise TimesUpTypeException(error_code=31, incorrect_input="permissions")
        if self.username == "":
            raise TimesUpEmptyFieldException(error_code=32, blank_field="username")
        if self.password == "" or self.password is None:
            raise TimesUpEmptyFieldException(error_code=33, blank_field="password")
        if self.email == "" or self.email is None:
            raise TimesUpEmptyFieldException(error_code=34, blank_field="email")

    def get_id(self):
        return self.user_id

    def has_permissions(self, permissions):
        return set(permissions) <= set(self.permissions)

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, User)