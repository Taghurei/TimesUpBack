from games.manager import GameManager
from games.model import Game


def get_all_games():
    games = GameManager().get_all()
    return games


def insert_game(inputs: dict):
    game_manager = GameManager()
    game_to_insert = Game(**inputs)
    game_manager.insert_one(game_to_insert)
    return game_to_insert
