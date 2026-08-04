from core.model import Document

from core.exceptions import (
    TimesUpEmptyFieldException,
    TimesUpTypeException,
    TimesUpUnexpectedNegativeValue,
)

from games.exceptions import TimesUpTeamsException

# A lobby is a game a host opened and that players are still joining: it is
# allowed to be empty. A started game has to be complete enough to be played.
LOBBY = "lobby"
STARTED = "started"
STATUSES = [LOBBY, STARTED]

TEAMS = ["team1", "team2"]


class Game(Document):
    fields = Document.fields + [
        "name",
        "words",
        "teams",
        "timer",
        "owner",
        "status",
    ]
    export_fields = Document.export_fields + [
        "game_id",
        "name",
        "words",
        "teams",
        "timer",
        "owner",
        "status",
    ]

    editable_fields = Document.editable_fields + [
        "words",
        "teams",
        "timer",
        "status",
        "updated_at",
    ]

    def __init__(
        self,
        game_id: str = "",
        name: str = "",
        words: list = None,
        teams: dict = None,
        timer: int = 30,
        owner: str = "",
        status: str = STARTED,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.game_id = self._id
        self.name = name
        # words and teams grow as players join, so every game needs its own
        self.words = [] if words is None else words
        self.teams = {"team1": [], "team2": []} if teams is None else teams
        self.timer = timer
        self.owner = owner
        self.status = status
        self.verify()

    def verify(self):
        super().verify()
        if not isinstance(self.name, str):
            raise TimesUpTypeException(error_code=2, incorrect_input="name")

        if self.name == "" or self.name is None:
            raise TimesUpEmptyFieldException(error_code=3, blank_field="name")

        if not isinstance(self.words, list):
            raise TimesUpTypeException(error_code=4, incorrect_input="words")

        if not isinstance(self.teams, dict):
            raise TimesUpTypeException(error_code=6, incorrect_input="teams")

        if not isinstance(self.timer, int):
            raise TimesUpTypeException(error_code=8, incorrect_input="timer")

        if self.timer < 1:
            raise TimesUpUnexpectedNegativeValue(error_code=9, incorrect_input="timer")

        if not isinstance(self.owner, str):
            raise TimesUpTypeException(error_code=34, incorrect_input="owner")

        if self.status not in STATUSES:
            raise TimesUpTypeException(error_code=35, incorrect_input="status")

        self.verify_teams()

        if self.status == LOBBY:
            return

        if len(self.words) < 1:
            raise TimesUpEmptyFieldException(error_code=5, blank_field="words")

        if len(self.teams["team1"]) < 1 or len(self.teams["team2"]) < 1:
            raise TimesUpTeamsException(error_code=7)

    def verify_teams(self):
        """Teams always have the right shape, even while the lobby is still empty."""
        if (
            not "team1" in self.teams
            or not "team2" in self.teams
            or (
                not isinstance(self.teams["team1"], list)
                or not isinstance(self.teams["team2"], list)
                or len(self.teams) != 2
            )
        ):
            raise TimesUpTeamsException(error_code=7)

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, Game)
