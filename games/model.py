from core.model import Document
from core.utils import slug


class Game(Document):
    fields = Document.fields + [
        "name",
        "words",
        "teams",
        "timer",
    ]
    export_fields= Document.export_fields +[
        "name",
        "words",
        "teams",
        "timer",
    ]
    def __init__(
        self,
        name: str = "",
        words: list = [],
        teams: list = [],
        timer: int = 30,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.words = words
        self.teams = teams
        self.timer = timer

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Game)
