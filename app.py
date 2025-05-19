import json
import random

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load skins
with open("skins.json") as f:
    skins = json.load(f)

skin_files = list(skins.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    if "current_skin" not in session:
        session["current_skin"] = random.choice(skin_files)
        session["streak"] = session.get("streak", 0)

    skin_file = session["current_skin"]
    correct_name = skins[skin_file]

    result = None
    correct = False
    surrendered = False

    if request.method == "POST":
        user_guess = request.form.get("guess", "").strip().lower()
        if "surrender" in request.form:
            result = f"The correct answer was: {correct_name}"
            surrendered = True
            session["streak"] = 0
        elif user_guess == correct_name.lower():
            result = "Correct!"
            correct = True
            session["streak"] = session.get("streak", 0) + 1
        else:
            result = "Wrong guess. Try again."

    return render_template(
        "index.html",
        skin_file=skin_file,
        result=result,
        correct=correct,
        surrendered=surrendered,
        streak=session.get("streak", 0),
    )


@app.route("/next")
def next_image():
    session["current_skin"] = random.choice(skin_files)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
