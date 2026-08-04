from flask import Flask, render_template, json, jsonify
from core.exceptions import TimesUpException
from routes.auth import auth
from routes.games import games
from routes.players import players
from routes.words import words
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(auth)
app.register_blueprint(games)
app.register_blueprint(players)
app.register_blueprint(words)
app.config["MONGO_URI"] = os.environ.get(
    "MONGO_URI", "mongodb://localhost:27017/test?retryWrites=true&w=majority"
)
# signs the login tokens: set TIMESUP_SECRET in production, or every restart
# logs everybody out
app.config["SECRET_KEY"] = os.environ.get("TIMESUP_SECRET", "timesup-dev-secret")
app.mongo = PyMongo(app)

try:
    with app.app_context():
        app.mongo.db.users.create_index("nickname", unique=True)
except Exception as error:
    # the app used to boot without a reachable mongo, keep it that way
    print("Could not create the users index:", error)


@app.errorhandler(TimesUpException)
def handle_timesup_exception(error):
    """Send our own errors back as json so the front can show them."""
    return (
        jsonify({"error_code": error.error_code, "message": error.external_message}),
        error.status_code,
    )


@app.route("/")
def home_page():
    return "Back is Up"
