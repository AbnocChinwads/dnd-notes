import os
from os import path
from flask import (Flask, flash, render_template,
                   redirect, request, url_for, Blueprint)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if path.exists("env.py"):
    import env

app = Flask(__name__)
mod = Blueprint("games", __name__)

app.config["MONGO_DBNAME"] = "dnd-project"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)


@app.route("/user", methods=["GET"])
def user(users_id):
    users = mongo.db.users.find_one({
                                     "_id": ObjectId(users_id)
                                     })
    user = users.username
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), debug=True)
