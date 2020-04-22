from players.manager import PlayerManager
from players.model import Player


def get_all_players():
    players = PlayerManager().get_all()
    return players


def update_player(player_id: str, inputs: dict):
    player_manager = PlayerManager()
    player_to_update = player_manager.get(player_id)
    player_to_update.update(inputs)

    player_manager.update_one(player_to_update)
    return player_to_update


def insert_player(inputs: dict):
    player_manager = PlayerManager()
    player_to_insert = Player(**inputs)
    player_manager.insert_one(player_to_insert)
    return player_to_insert
