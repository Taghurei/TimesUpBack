from core.model import Document

from core.exceptions import (
    TimesUpEmptyFieldException,
    TimesUpTypeException,
    TimesUpUnexpectedNegativeValue,
)


class Player(Document):
    fields = Document.fields + [
        "name",
        "score_total",
        "score_round",
    ]
    export_fields = Document.export_fields + [
        "player_id",
        "name",
        "score_total",
        "score_round",
    ]

    editable_fields = Document.editable_fields + [
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
        self.verify()

    def verify(self):
        if not isinstance(self.player_id, str):
            raise TimesUpTypeException(error_code=10, incorrect_input="player_id")

        if not isinstance(self.name, str):
            raise TimesUpTypeException(error_code=12, incorrect_input="name")

        if self.name == "" or self.name is None:
            raise TimesUpEmptyFieldException(error_code=13, blank_field="name")

        if not isinstance(self.score_total, int):
            raise TimesUpTypeException(error_code=14, incorrect_input="score_total")

        if self.score_total < 0:
            raise TimesUpUnexpectedNegativeValue(
                error_code=15, incorrect_input="score_total"
            )

        if not isinstance(self.score_round, int):
            raise TimesUpTypeException(error_code=16, incorrect_input="score_round")

        if self.score_round < 0:
            raise TimesUpUnexpectedNegativeValue(
                error_code=17, incorrect_input="score_round"
            )

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Player)
