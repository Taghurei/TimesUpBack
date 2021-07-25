from flask import Blueprint, jsonify, current_app, request
from flask_login import login_required

import users.controller as ctrl

users = Blueprint("users", __name__)

@users.route("/login", methods=["POST"])
def login():
    inputs = request.json
    user = ctrl.login(inputs)
    return jsonify(user.to_dict())

@users.route("/signup", methods=["POST"])
def signup():
    print('biujour')
    inputs = request.json
    current_app.logger.debug(inputs)
    print('****')
    print(inputs)
    print('*****')
    user = ctrl.signup(inputs)
    return jsonify(user.to_dict())


@users.route("/logout")
@login_required
def logout():
    ctrl.logout()
    return jsonify({"status": "Logout successfully"})