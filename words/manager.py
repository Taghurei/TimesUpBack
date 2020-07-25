from core.manager import MongoManager
from words.model import Word


class WordManager(MongoManager):
    def __init__(self):
        super().__init__("words")

    def get_all(self):
        return [Word.from_dict(x) for x in super().get_all()]

    def get(self, word_id):
        return Word.from_dict(super().get(word_id))

    def get_by_name(self, word_name):
        return Word.from_dict(super().get_by_name(word_name))

    def update_one(self, word):
        return super().update_one(word.word_id, word.to_insert_dict())

    def insert_one(self, word):
        return super().insert_one(word.to_insert_dict())

    def remove_one(self, word):
        return super().remove_one(word.word_id)
