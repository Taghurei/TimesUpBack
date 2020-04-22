from flask import Blueprint, jsonify, request
from players.controller import (
    get_all_players,
    update_player,
    insert_player,
)

players = Blueprint("players", __name__)


@players.route("/players")
def get_players():
    players = get_all_players()
    return jsonify([p.to_dict() for p in players])


@players.route("/players/<player_id>", methods=["POST"])
def post_player(player_id: str):
    update_dict = request.json
    updated = update_player(player_id, update_dict)
    return jsonify(updated.to_dict())


@players.route("/players", methods=["POST"])
def put_player():
    insert_dict = request.json
    inserted = insert_player(insert_dict)
    return jsonify(inserted.to_dict())
