from core.model import Document

from core.exceptions import (
    TimesUpEmptyFieldException,
    TimesUpTypeException,
    TimesUpUnexpectedNegativeValue,
)

from games.exceptions import TimesUpTeamsException


class Game(Document):
    fields = Document.fields + [
        "name",
        "words",
        "teams",
        "timer",
    ]
    export_fields = Document.export_fields + [
        "name",
        "words",
        "teams",
        "timer",
    ]

    def __init__(
        self,
        name: str = "",
        words: list = [],
        teams: dict = {"teams1": [], "teams2": []},
        timer: int = 30,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.words = words
        self.teams = teams
        self.timer = timer
        self.verify()

    def verify(self):
        super().verify()
        if not isinstance(self.name, str):
            raise TimesUpTypeException(error_code=2, incorrect_input="name")

        if self.name == "" or self.name is None:
            raise TimesUpEmptyFieldException(error_code=3, blank_field="name")

        if not isinstance(self.words, list):
            raise TimesUpTypeException(error_code=4, incorrect_input="words")

        if len(self.words) < 1:
            raise TimesUpEmptyFieldException(error_code=5, blank_field="words")

        if not isinstance(self.teams, dict):
            raise TimesUpTypeException(error_code=6, incorrect_input="teams")

        if not "team1" in self.teams or not "team2" in self.teams or (
            not isinstance(self.teams["team1"], list)
            or not isinstance(self.teams["team2"], list)
            or len(self.teams["team1"]) < 1
            or len(self.teams["team2"]) < 1
            or len(self.teams) != 2
        ):
            raise TimesUpTeamsException(error_code=7)

        if not isinstance(self.timer, int):
            raise TimesUpTypeException(error_code=8, incorrect_input="timer")

        if self.timer < 1:
            raise TimesUpUnexpectedNegativeValue(error_code=9, incorrect_input="timer")

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Game)
