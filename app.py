import os
from flask import (Flask, flash, render_template,
                   redirect, request, url_for, Blueprint)

app = Flask(__name__)
mod = Blueprint("games", __name__)


@app.route("/", methods=["GET", "POST"])
def index():
    users = request.form.get("user")
    if users == "user":
        return redirect("user")
    return render_template("index.html", user=users)


@app.route("/user")
def user():
    return render_template("user.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), debug=True)
