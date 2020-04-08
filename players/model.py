from core.model import Document
from core.utils import slug


class Player(Document):
    fields = Document.fields + [
        "name",
        "score",
    ]
    export_fields= Document.export_fields +[
        "player_id",
        "name",
        "score",
    ]

    editable_fields= Document.editable_fields +[
        "player_id",
        "name",
        "score",
    ]
    def __init__(
        self,
        player_id: str = "",
        name: str = "",
        score: int = 0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.player_id = self._id
        self.name = name
        self.score = score

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Player)
