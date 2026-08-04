from uuid import uuid4

from core.exceptions import TimesUpTypeException
from games.exceptions import (
    TimesUpEmptyLobbyException,
    TimesUpGameAlreadyStartedException,
    TimesUpGameNotFoundException,
    TimesUpMissingPlayerNameException,
    TimesUpNotGameOwnerException,
    TimesUpUnknownTeamException,
)
from games.manager import GameManager
from games.model import LOBBY, STARTED, TEAMS, Game
from players.controller import insert_player
from players.manager import PlayerManager
from words.controller import add_words


def get_all_games():
    games = GameManager().get_all()
    return games


def insert_game(inputs: dict, owner: str = ""):
    """Create a game that is ready to be played right away, without a lobby."""
    game_manager = GameManager()
    # owner and status are never taken from the request: they decide who may
    # start a game, so only the back sets them
    game_inputs = {key: inputs[key] for key in inputs if key not in ["owner", "status"]}
    game_to_insert = Game(owner=owner, status=STARTED, **game_inputs)
    game_manager.insert_one(game_to_insert)
    return game_to_insert


def create_lobby(owner: str, timer: int = 30):
    """Open a game the host's friends can join with the host's nickname."""
    game_manager = GameManager()
    already_open = game_manager.get_lobby_by_owner(owner)
    if already_open:
        return already_open

    lobby = Game(
        name=owner + "-" + uuid4().hex[:6],
        owner=owner,
        timer=timer,
        status=LOBBY,
    )
    game_manager.insert_one(lobby)
    return lobby


def get_lobby(owner: str):
    lobby = GameManager().get_lobby_by_owner(owner)
    if not lobby:
        raise TimesUpGameNotFoundException()
    return lobby


def get_game(game_id: str):
    game = GameManager().get(game_id)
    if not game:
        raise TimesUpGameNotFoundException()
    return game


def add_words_to_game(game_id: str, new_words: list):
    """Everybody in the lobby feeds the same word pool, duplicates aside."""
    game = get_open_lobby(game_id)
    if not isinstance(new_words, list):
        raise TimesUpTypeException(error_code=4, incorrect_input="words")

    known_words = {word.lower() for word in game.words}
    for new_word in new_words:
        if not isinstance(new_word, str) or not new_word.strip():
            continue
        word = new_word.strip()
        if word.lower() not in known_words:
            game.words.append(word)
            known_words.add(word.lower())

    return save(game)


def join_game(game_id: str, player_name: str, team: str):
    """Add a player to one of the teams, or move them if they already joined."""
    game = get_open_lobby(game_id)
    if team not in TEAMS:
        raise TimesUpUnknownTeamException(team=team)
    if not isinstance(player_name, str) or not player_name.strip():
        raise TimesUpMissingPlayerNameException()

    player_name = player_name.strip()
    already_in = find_player_by_name(game, player_name)
    if already_in:
        player, current_team = already_in
        if current_team == team:
            return game, player
        game.teams[current_team].remove(player.player_id)
        game.teams[team].append(player.player_id)
        return save(game), player

    player = insert_player({"name": player_name})
    game.teams[team].append(player.player_id)
    return save(game), player


def start_game(game_id: str, owner: str, timer=None):
    """Close the lobby and turn it into a playable game. Host only."""
    game = get_game(game_id)
    if not game.owner or game.owner != owner:
        raise TimesUpNotGameOwnerException()
    if game.status != LOBBY:
        raise TimesUpGameAlreadyStartedException()
    if len(game.words) < 1:
        raise TimesUpEmptyLobbyException()

    if timer is not None:
        game.timer = timer
    game.status = STARTED
    # saving re-runs verify, which also demands a player in each team
    return save(game)


def game_state(game):
    """The game as the lobby needs it: players resolved so their names show up."""
    player_manager = PlayerManager()
    players = {}
    for team in TEAMS:
        team_players = [player_manager.get(_id) for _id in game.teams[team]]
        players[team] = [player.to_dict() for player in team_players if player]
    return dict(game.to_dict(), players=players)


def get_open_lobby(game_id: str):
    game = get_game(game_id)
    if game.status != LOBBY:
        raise TimesUpGameAlreadyStartedException()
    return game


def find_player_by_name(game, player_name: str):
    player_manager = PlayerManager()
    for team in TEAMS:
        for player_id in game.teams[team]:
            player = player_manager.get(player_id)
            if player and player.name == player_name:
                return player, team
    return None


def save(game):
    game.update({})
    GameManager().update_one(game)
    return game


def populate_games():
    games = GameManager().get_all()
    word_list = []
    for game in games:
        word_list = word_list + game.words
    add_words("test", word_list)
