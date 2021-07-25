from flask import Flask, render_template, json
from routes.games import games
from routes.players import players
from routes.words import words
from routes.users import users
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_login import LoginManager, current_user
from flask.logging import create_logger

import os

USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]
SECRET_KEY = os.environ["SECRET_KEY"]
app = Flask(__name__)
CORS(app)
app.secret_key = SECRET_KEY

app.config[
    "MONGO_URI"
] = "mongodb+srv://{}:{}@cluster0-wam2v.mongodb.net/test?retryWrites=true&w=majority".format(
    USER, PASSWORD
)
app.mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.logger = create_logger(app)
app.register_blueprint(games)
app.register_blueprint(players)
app.register_blueprint(words)
app.register_blueprint(users)
@app.route("/")
def home_page():
    return "Back is Up"
