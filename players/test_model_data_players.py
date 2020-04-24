from core.exceptions import (
    TimesUpDateException,
    TimesUpEmptyFieldException,
    TimesUpUnexpectedNegativeValue,
    TimesUpTypeException,
)

correct_players_data = [
    (
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        # Object can be updated after it was created
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 10,
        },
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 10,
        },
    ),
]

incorrect_players_data = [
    (
        # can't have created_at after updated_at
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": 5,
            "updated_at": 0,
        },
        TimesUpDateException,
    ),
    (
        # can't have created_at after updated_at
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "player_name",
            "score_total": 0,
            "score_round": 0,
            "created_at": None,
            "updated_at": 5,
        },
        TimesUpDateException,
    ),
    (
        # can't have empty name
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "",
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # name must be a string
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": {"name": "name"},
            "score_total": 0,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # score_total must be an int
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "name",
            "score_total": "0",
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # score_total must be positive
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "name",
            "score_total": -10,
            "score_round": 0,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpUnexpectedNegativeValue,
    ),
    (
        # score_round must be an int
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "name",
            "score_total": 0,
            "score_round": "0",
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # score_round must be positive
        {
            "_id": "player_id",
            "player_id": "player_id",
            "name": "name",
            "score_total": 0,
            "score_round": -10,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpUnexpectedNegativeValue,
    ),
]
