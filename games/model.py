from core.model import Document
from core.utils import slug


class Game(Document):
    fields = Document.fields + [
        "name",
        "words",
        "teams",
    ]
    export_fields= Document.export_fields +[
        "name",
        "words",
        "teams",      
    ]
    def __init__(
        self,
        name: str = "",
        words: list = [],
        teams: list = [],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.words = words
        self.teams = teams

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Game)
