import json
import random

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

with open("skins.json", "r") as f:
    skins = json.load(f)

skin_files = list(skins.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    if "current_skin" not in session:
        session["current_skin"] = random.choice(skin_files)

    skin_file = session["current_skin"]
    correct_name = skins[skin_file]
    result = None

    if request.method == "POST":
        if "surrender" in request.form:
            result = f"The correct answer was: {correct_name}"
        elif "guess" in request.form:
            user_guess = request.form["guess"].strip().lower()
            if user_guess == correct_name.lower():
                result = "Correct!"
            else:
                result = "Wrong guess. Try again."

    return render_template(
        "index.html", skin_file=skin_file, result=result, correct=(result == "Correct!")
    )


@app.route("/next")
def next_image():
    session["current_skin"] = random.choice(skin_files)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
