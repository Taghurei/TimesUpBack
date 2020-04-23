import time

import pytest

from games.model import Game
from games.test_model_data import correct_games_data, incorrect_games_data


def get_game(test_input):
    return Game(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        name=test_input["name"],
        words=test_input["words"],
        teams=test_input["teams"],
        timer=test_input["timer"],
    )


class TestInit:
    @pytest.mark.parametrize("test_input,expected", correct_games_data)
    def test_game_legit_args(self, test_input, expected):
        game = get_game(test_input)

        assert game._id == expected["_id"]
        assert game.created_at == expected["created_at"]
        assert game.updated_at == expected["updated_at"]
        assert game.name == expected["name"]
        assert game.words == expected["words"]
        assert game.teams == expected["teams"]
        assert game.timer == expected["timer"]

    @pytest.mark.parametrize("test_input,error_raised", incorrect_games_data)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            game = get_game(test_input)
