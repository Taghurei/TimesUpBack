from core.model import Document

from core.exceptions import (
    TimesUpEmptyFieldException,
    TimesUpTypeException,
)


class User(Document):
    fields = Document.fields + [
        "nickname",
        "password_hash",
    ]
    # password_hash is never exported: it must not leave the back
    export_fields = Document.export_fields + [
        "user_id",
        "nickname",
    ]

    editable_fields = Document.editable_fields + [
        "password_hash",
    ]

    def __init__(
        self,
        user_id: str = "",
        nickname: str = "",
        password_hash: str = "",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.user_id = self._id
        self.nickname = nickname
        self.password_hash = password_hash
        self.verify()

    def verify(self):
        super().verify()
        if not isinstance(self.nickname, str):
            raise TimesUpTypeException(error_code=26, incorrect_input="nickname")

        if self.nickname == "" or self.nickname is None:
            raise TimesUpEmptyFieldException(error_code=27, blank_field="nickname")

        if not isinstance(self.password_hash, str):
            raise TimesUpTypeException(error_code=28, incorrect_input="password_hash")

        if self.password_hash == "" or self.password_hash is None:
            raise TimesUpEmptyFieldException(error_code=29, blank_field="password_hash")

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, User)
