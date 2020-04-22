from core.model import Document


class Player(Document):
    fields = Document.fields + [
        "name",
        "score_total",
        "score_round",
    ]
    export_fields= Document.export_fields +[
        "player_id",
        "name",
        "score_total",
        "score_round",
    ]

    editable_fields= Document.editable_fields +[
        "player_id",
        "name",
        "score_total",
        "score_round",
    ]
    def __init__(
        self,
        player_id: str = "",
        name: str = "",
        score_total: int = 0,
        score_round: int = 0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.player_id = self._id
        self.name = name
        self.score_total = score_total
        self.score_round = score_round

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Player)
