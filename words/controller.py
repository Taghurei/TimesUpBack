from words.manager import WordManager
from words.model import Word


def get_all_words():
    words = WordManager().get_all()
    return words


def update_word(word_id: str, inputs: dict):
    word_manager = WordManager()
    word_to_update = word_manager.get(word_id)
    word_to_update.update(inputs)

    word_manager.update_one(word_to_update)
    return word_to_update


def insert_word(inputs: dict):
    word_manager = WordManager()
    word_to_insert = word(**inputs)
    word_manager.insert_one(word_to_insert)
    return word_to_insert
