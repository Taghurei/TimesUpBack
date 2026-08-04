from core.exceptions import (
    TimesUpDateException,
    TimesUpEmptyFieldException,
    TimesUpTypeException,
)

correct_users_data = [
    (
        {
            "_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "user_id",
            "user_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        # Object can be updated after it was created
        {
            "_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 10,
        },
        {
            "_id": "user_id",
            "user_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 10,
        },
    ),
]

incorrect_users_data = [
    (
        # can't have created_at after updated_at
        {
            "_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "hashed_password",
            "created_at": 5,
            "updated_at": 0,
        },
        TimesUpDateException,
    ),
    (
        # can't have an empty nickname
        {
            "_id": "user_id",
            "nickname": "",
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # nickname must be a string
        {
            "_id": "user_id",
            "nickname": ["gauthier"],
            "password_hash": "hashed_password",
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
    (
        # a user without a password can't log in
        {
            "_id": "user_id",
            "nickname": "gauthier",
            "password_hash": "",
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # password_hash must be a string
        {
            "_id": "user_id",
            "nickname": "gauthier",
            "password_hash": 1234,
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
]
