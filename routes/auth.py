from flask import Blueprint, g, jsonify, request

from users.auth import login_required
from users.controller import login_user, register_user

auth = Blueprint("auth", __name__)


@auth.route("/auth/register", methods=["POST"])
def post_register():
    inputs = request.json or {}
    user, token = register_user(inputs.get("nickname"), inputs.get("password"))
    return jsonify(dict(user.to_dict(), token=token))


@auth.route("/auth/login", methods=["POST"])
def post_login():
    inputs = request.json or {}
    user, token = login_user(inputs.get("nickname"), inputs.get("password"))
    return jsonify(dict(user.to_dict(), token=token))


@auth.route("/auth/me")
@login_required
def get_me():
    return jsonify(g.current_user.to_dict())
