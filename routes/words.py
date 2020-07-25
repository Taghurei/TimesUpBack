from flask import Blueprint, jsonify, request

from words.controller import get_all_words, get_one_word

words = Blueprint("words", __name__)


@words.route("/words")
def get_words():
    words = get_all_words()
    return jsonify([g.to_dict() for g in words])

@words.route("/words/<word_name>")
def get_words_by_name(word_name):
    words = get_one_word(word_name)
    return jsonify(words)
