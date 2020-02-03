from flask import Flask, request, render_template
from flask.load_token_dic import load_english_dic, load_japanese_dic
from flask.utils.text_preprocess import normalize_english
from flask.utils.dataset import tokenize
from flask.utils.model import decoder_seq
from load_token_dic import *
import tensorflow as tf

# define model
model = tf.keras.models.load_model("path")

# load word token dic
english_tokens = load_english_dic()
japanese_tokens = load_japanese_dic()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translation", methods=["POST", "GET"])
def translate():
    result = {}

    if request.method == "POST":

        # input lang
        input_lang = request.form["input_lang"]
        result["input"] = input_lang

        # translate lang
        input_lang = normalize_english(input_lang)
        # create input value for encode
        encoder_input = tokenize(input_lang, english_tokens)

        # predict
        result["predict"] = decoder_seq(model, encoder_input, japanese_tokens)

        return render_template("translate.html", lang=result)


if __name__ == "__main__":
    app.run(debug=True)