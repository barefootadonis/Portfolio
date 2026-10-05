from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print(name)
        print(email)
        print(message)

        success = True

    return render_template(
        "contact.html",
        success=success
    )


@app.context_processor
def inject_globals():
    return {
        "current_year": datetime.now().year
    }


if __name__ == "__main__":
    app.run(debug=True)