import pytest

from core.exceptions import TimesUpEmptyFieldException, TimesUpTypeException
from games.exceptions import TimesUpTeamsException
from games.model import LOBBY, STARTED, Game

EMPTY_TEAMS = {"team1": [], "team2": []}
FULL_TEAMS = {"team1": ["player1"], "team2": ["player2"]}


def get_lobby(**kwargs):
    arguments = dict(
        _id="game_id",
        created_at=0,
        updated_at=0,
        name="game_name",
        owner="gauthier",
        status=LOBBY,
    )
    arguments.update(kwargs)
    return Game(**arguments)


class TestLobby:
    def test_a_lobby_starts_empty(self):
        lobby = get_lobby()

        assert lobby.status == LOBBY
        assert lobby.owner == "gauthier"
        assert lobby.words == []
        assert lobby.teams == EMPTY_TEAMS

    def test_a_lobby_keeps_its_teams_shape(self):
        with pytest.raises(TimesUpTeamsException):
            get_lobby(teams={"team1": [], "team3": []})

    def test_a_lobby_still_needs_a_name(self):
        with pytest.raises(TimesUpEmptyFieldException):
            get_lobby(name="")

    def test_status_must_be_known(self):
        with pytest.raises(TimesUpTypeException):
            get_lobby(status="whatever")

    def test_owner_must_be_a_string(self):
        with pytest.raises(TimesUpTypeException):
            get_lobby(owner=["gauthier"])

    def test_game_id_is_exported_so_players_can_join(self):
        assert get_lobby().to_dict()["game_id"] == "game_id"

    def test_two_games_do_not_share_their_word_list(self):
        first = get_lobby()
        second = get_lobby()

        first.words.append("word")

        assert second.words == []
        assert second.teams == EMPTY_TEAMS


class TestStarting:
    def test_a_started_game_needs_words(self):
        lobby = get_lobby(teams=FULL_TEAMS)
        lobby.status = STARTED

        with pytest.raises(TimesUpEmptyFieldException):
            lobby.verify()

    def test_a_started_game_needs_players_in_both_teams(self):
        lobby = get_lobby(words=["word"], teams={"team1": ["player1"], "team2": []})
        lobby.status = STARTED

        with pytest.raises(TimesUpTeamsException):
            lobby.verify()

    def test_a_filled_lobby_can_start(self):
        lobby = get_lobby(words=["word"], teams=FULL_TEAMS)
        lobby.status = STARTED

        lobby.verify()

        assert lobby.to_dict()["status"] == STARTED

    def test_a_game_is_started_by_default(self):
        game = Game(name="game_name", words=["word"], teams=FULL_TEAMS)

        assert game.status == STARTED
        assert game.owner == ""
