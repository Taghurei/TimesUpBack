import time

import pytest

from words.model import Word
from words.test_model_data_words import correct_words_data, incorrect_words_data


def get_word(test_input):
    return Word(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        name=test_input["name"],
        words=test_input["words"],
    )


class TestInit:
    @pytest.mark.parametrize("test_input,expected", correct_words_data)
    def test_word_legit_args(self, test_input, expected):
        word = get_word(test_input)

        assert word._id == expected["_id"]
        assert word.created_at == expected["created_at"]
        assert word.updated_at == expected["updated_at"]
        assert word.name == expected["name"]
        assert word.words == expected["words"]

    @pytest.mark.parametrize("test_input,error_raised", incorrect_words_data)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            word = get_word(test_input)
