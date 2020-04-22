from core.manager import MongoManager
from players.model import Player


class PlayerManager(MongoManager):
    def __init__(self):
        super().__init__("players")

    def get_all(self):
        return [Player.from_dict(x) for x in super().get_all()]

    def get(self, player_id):
        return Player.from_dict(super().get(player_id))

    def update_one(self, player):
        return super().update_one(player.player_id, player.to_insert_dict())

    def insert_one(self, player):
        return super().insert_one(player.to_insert_dict())

    def remove_one(self, player):
        return super().remove_one(player.player_id)
