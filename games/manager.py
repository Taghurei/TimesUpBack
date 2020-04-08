from core.manager import MongoManager
from games.model import Game


class GameManager(MongoManager):
    def __init__(self):
        super().__init__("games")

    def get_all(self):
        return [Game.from_dict(x) for x in super().get_all()]

    def insert_one(self, game):
        return super().insert_one(game.to_insert_dict())