from flask import Flask, render_template, json
from routes.games import games
from routes.players import players
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

user = os.environ['USER']
password = os.environ['PASSWORD']

app = Flask(__name__)
CORS(app)
app.register_blueprint(games)
app.register_blueprint(players)
app.config["MONGO_URI"] = "mongodb+srv://{user}:{password}@cluster0-wam2v.mongodb.net/test?retryWrites=true&w=majority"
app.mongo = PyMongo(app)
@app.route("/game")
def home_page():
    words_dict = app.mongo.db.words.find_one({"name":"GameTest"})
    print(type(words_dict))
    print((words_dict))
    del words_dict['_id']
    return json.dumps(words_dict)
