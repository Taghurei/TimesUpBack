from core.exceptions import (
    TimesUpDateException,
    TimesUpEmptyFieldException,
    TimesUpTypeException,
)

correct_words_data = [
    (
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        # Object can be updated after it was created
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 10,
        },
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 10,
        },
    ),
]

incorrect_words_data = [
    (
        # can't have created_at after updated_at
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": 5,
            "updated_at": 0,
        },
        TimesUpDateException,
    ),
    (
        # can't have created_at after updated_at
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "word_name",
            "words": ["word1"],
            "created_at": None,
            "updated_at": 5,
        },
        TimesUpDateException,
    ),
    (
        # name can't be empty
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "",
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
    (
        # name must be a string
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": ["name"],
            "words": ["word1"],
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
      (
        # words can't be empty
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "name",
            "words": [],
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpEmptyFieldException,
    ),
      (
        # words must be a list
        {
            "_id": "word_id",
            "word_id": "word_id",
            "name": "name",
            "words": {"word1":"word"},
            "created_at": 0,
            "updated_at": 0,
        },
        TimesUpTypeException,
    ),
]