from games.exceptions import TimesUpTeamsException
from core.exceptions import (
    TimesUpDateException,
    TimesUpEmptyFieldException,
    TimesUpUnexpectedNegativeValue,
    TimesUpTypeException,
)

correct_games_data = [
    (
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        # Object can be updated after it was created
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 10,
        },
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 10,
        },
    ),
]
