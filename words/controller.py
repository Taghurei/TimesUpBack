from words.manager import WordManager
from words.model import Word


def get_all_words_dictionaries():
    words_lists = WordManager().get_all()
    words_dictionaries = {} 
    for word_list in words_lists:
        words_dictionary = word_list.to_dict()
        words_dictionaries[words_dictionary['name']] = words_dictionary['words'] 
    return words_dictionaries


def get_one_word(word_name):
    words = WordManager().get_by_name(word_name)
    return words.to_dict()["words"]


def add_words(word_name, word_list):
    words = WordManager().get_by_name(word_name)
    words.words = words.words + word_list
    word_manager = WordManager()
    print(words.to_dict())
    word_manager.update_one("5e9eb40f2443ad3d3c87c5e3", words)


def insert_word(inputs: dict):
    word_manager = WordManager()
    word_to_insert = word(**inputs)
    word_manager.insert_one(word_to_insert)
    return word_to_insert


def update_word(word_name: str, word_list: list):
    word_manager = WordManager()
    word_to_update = word_manager.get_by_name(word_name)
    word_to_update.words = word_list
    word_manager.update_one_by_name(word_name, word_to_update)
    return word_to_update
