from core.manager import MongoManager
from games.model import LOBBY, Game


class GameManager(MongoManager):
    def __init__(self):
        super().__init__("games")

    def get_all(self):
        return [Game.from_dict(x) for x in super().get_all()]

    def get(self, game_id):
        game = super().get(game_id)
        return Game.from_dict(game) if game else None

    def get_by_name(self, game_name):
        game = super().get_by_name(game_name)
        return Game.from_dict(game) if game else None

    def get_lobby_by_owner(self, owner):
        """The lobby a host currently has open, the most recent one if there are several."""
        game = super().get_one(
            {"owner": owner, "status": LOBBY}, sort=[("created_at", -1)]
        )
        return Game.from_dict(game) if game else None

    def insert_one(self, game):
        return super().insert_one(game.to_insert_dict())

    def update_one(self, game):
        return super().update_one(game.game_id, game.to_update_dict())
