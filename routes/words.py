from flask import Blueprint, jsonify, request

from words.controller import (
    get_all_words_dictionaries,
    get_one_word,
    update_word,
)

words = Blueprint("words", __name__)


@words.route("/words/")
def get_words_name():
    all_words = get_all_words_dictionaries()
    return jsonify(all_words)


@words.route("/words/<word_name>")
def get_words_by_name(word_name):
    words = get_one_word(word_name)
    return jsonify(words)


@words.route("/words/<word_name>", methods=["PUT"])
def update_words(word_name):
    update_dict = request.json
    words = update_word(word_name, update_dict)
    return jsonify(words.to_dict())
