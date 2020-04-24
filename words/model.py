from core.model import Document

from core.exceptions import (
    TimesUpEmptyFieldException,
    TimesUpTypeException,
)

class Word(Document):
    fields = Document.fields + [
        "name",
        "words",
    ]
    export_fields = Document.export_fields + [
        "name",
        "words",
    ]

    editable_fields = Document.editable_fields + [
        "name",
        "words",
    ]

    def __init__(self, word_id: str = "", name: str = "", words: list = [], **kwargs):
        super().__init__(**kwargs)
        self.word_id = self._id
        self.name = name
        self.words = words
        self.verify()

    def verify(self):
        if not isinstance(self.word_id, str):
            raise TimesUpTypeException(error_code=18, incorrect_input="word_id")

        if not isinstance(self.name, str):
            raise TimesUpTypeException(error_code=19, incorrect_input="name")

        if self.name == "" or self.name is None:
            raise TimesUpEmptyFieldException(error_code=20, blank_field="name")

        if not isinstance(self.words, list):
            raise TimesUpTypeException(error_code=21, incorrect_input="words")

        if len(self.words) < 1 :
            raise TimesUpEmptyFieldException(error_code=22, blank_field="words")

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Word)
