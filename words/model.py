from core.model import Document


class Word(Document):
    fields = Document.fields + [
        "name",
        "words",
    ]
    export_fields= Document.export_fields +[
        "name",
        "words",
    ]

    editable_fields= Document.editable_fields +[
        "name",
        "words",
    ]
    def __init__(
        self,
        word_id: str = "",
        name: str = "",
        words: list = [],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.word_id = self._id
        self.name = name
        self.words = words

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Word)
