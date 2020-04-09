from flask import Flask, render_template, json
from routes.games import games
from routes.players import players
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
app = Flask(__name__)
CORS(app)
app.register_blueprint(games)
app.register_blueprint(players)
app.config["MONGO_URI"] = "mongodb+srv://{}:{}@cluster0-wam2v.mongodb.net/test?retryWrites=true&w=majority".format(USER,PASSWORD)
app.mongo = PyMongo(app)
@app.route("/")
def home_page():
    return "Back is Up"
