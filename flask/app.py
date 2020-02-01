from flask import Flask, request, render_template
from utils.text_preprocess import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translation", methods=["POST", "GET"])
def translate():
    if request.method == "POST":
        lang = request.form["input_lang"]
        lang = normalize_english(lang)
        return render_template("translate.html", lang=lang)


if __name__ == "__main__":
    app.run(debug=True)