from flask import Blueprint, jsonify, request

from words.controller import get_all_words

words = Blueprint("words", __name__)


@words.route("/words")
def get_words():
    words = get_all_words()
    return jsonify([g.to_dict() for g in words])
