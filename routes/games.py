from flask import Blueprint, g, jsonify, request

from games.controller import (
    add_words_to_game,
    create_lobby,
    game_state,
    get_all_games,
    get_game,
    get_lobby,
    insert_game,
    join_game,
    populate_games,
    start_game,
)
from users.auth import get_current_user, login_required

games = Blueprint("games", __name__)


@games.route("/games")
def get_games():
    all_games = get_all_games()
    return jsonify([game.to_dict() for game in all_games])


@games.route("/games", methods=["POST"])
def put_game():
    insert_dict = request.json or {}
    # a guest can still create a game without logging in
    user = get_current_user()
    inserted = insert_game(insert_dict, owner=user.nickname if user else "")
    return jsonify(inserted.to_dict())


@games.route("/games/populate")
def pop_games():
    populated_games = populate_games()
    return jsonify([game.to_dict() for game in populated_games])


@games.route("/games/lobby", methods=["POST"])
@login_required
def post_lobby():
    """Open a lobby other players will find with the host's nickname."""
    inputs = request.json or {}
    lobby = create_lobby(g.current_user.nickname, timer=inputs.get("timer", 30))
    return jsonify(game_state(lobby))


@games.route("/games/lobby/<nickname>")
def get_lobby_of(nickname):
    return jsonify(game_state(get_lobby(nickname)))


@games.route("/games/<game_id>")
def get_game_by_id(game_id):
    return jsonify(game_state(get_game(game_id)))


@games.route("/games/<game_id>/words", methods=["POST"])
def post_game_words(game_id):
    inputs = request.json or {}
    return jsonify(game_state(add_words_to_game(game_id, inputs.get("words", []))))


@games.route("/games/<game_id>/players", methods=["POST"])
def post_game_player(game_id):
    inputs = request.json or {}
    game, player = join_game(game_id, inputs.get("name"), inputs.get("team"))
    return jsonify(dict(game_state(game), player=player.to_dict()))


@games.route("/games/<game_id>/start", methods=["POST"])
@login_required
def post_game_start(game_id):
    inputs = request.json or {}
    started = start_game(
        game_id, g.current_user.nickname, timer=inputs.get("timer")
    )
    return jsonify(game_state(started))
