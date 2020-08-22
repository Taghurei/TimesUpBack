from flask import Blueprint, jsonify, request

from games.controller import (
    get_all_games,
    insert_game,
    populate_games,
)

games = Blueprint("games", __name__)


@games.route("/games")
def get_games():
    games = get_all_games()
    return jsonify([g.to_dict() for g in games])


@games.route("/games", methods=["POST"])
def put_game():
    insert_dict = request.json
    inserted = insert_game(insert_dict)
    return jsonify(inserted.to_dict())

@games.route("/games/populate")
def pop_games():
    games = populate_games()
    return jsonify([g.to_dict() for g in games])