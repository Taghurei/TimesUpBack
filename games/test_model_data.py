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

incorrect_games_data = [
    (
        # can't have created_at after updated_at
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 5,
            "updated_at": 0,
        },
        TimesUpDateException,
    ),
    (
        # can't have created_at after updated_at
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": None,
            "updated_at": 5,
        },
        TimesUpDateException,
    ),
    (
        # can't have empty name
        {
            "_id": "game_id",
            "name": "",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # name must be a string
        {
            "_id": "game_id",
            "name": ["game_name"],
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # can't have empty words
        {
            "_id": "game_id",
            "name": "game_name",
            "words": [],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # words must be a liste
        {
            "_id": "game_id",
            "name": "game_name",
            "words": {"word1": "word"},
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # teams must be an object
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": ["player1", "player2"],
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # Teams must have 2 keys
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"], "team3": ["player3"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # Teams must have team1 as a key
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team2": ["player2"], "team3": ["player3"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # Teams must have team2 as a key
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team3": ["player3"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # team1 must be a list
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": "player2", "team2": ["player3"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # team2 must be a list
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team2": "player2", "team1": ["player3"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # team1 must have at least 1 player
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": [], "team2": ["player2"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # team2 must have at least 1 player
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team2": [], "team1": ["player1"]},
            "timer": 30,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTeamsException,
    ),
    (
        # timer must be an int
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": "30",
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # timer must be positive
        {
            "_id": "game_id",
            "name": "game_name",
            "words": ["word"],
            "teams": {"team1": ["player1"], "team2": ["player2"]},
            "timer": -5,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpUnexpectedNegativeValue,
    ),
]
