import time

import pytest

from players.model import Player
from players.test_model_data_players import (
    correct_players_data,
    incorrect_players_data,
)


def get_player(test_input):
    return Player(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        name=test_input["name"],
        score_total=test_input["score_total"],
        score_round=test_input["score_round"],
    )


class TestInit:
    @pytest.mark.parametrize("test_input,expected", correct_players_data)
    def test_player_legit_args(self, test_input, expected):
        player = get_player(test_input)

        assert player._id == expected["_id"]
        assert player.created_at == expected["created_at"]
        assert player.updated_at == expected["updated_at"]
        assert player.name == expected["name"]
        assert player.score_total == expected["score_total"]
        assert player.score_round == expected["score_round"]

    @pytest.mark.parametrize("test_input,error_raised", incorrect_players_data)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            player = get_player(test_input)
