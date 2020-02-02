from flask import Flask, request, render_template
from utils.text_preprocess import *
from utils.model import *
from utils.dataset import *


import tensorflow as tf

# define model
# model = tf.keras.models.load_model("saver")


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
        encoder_input = convert_to_nparray(input_lang)

        # predict
        result["predict"] = decoder_seq(model, encoder_input)



        return render_template("translate.html", lang=result)


if __name__ == "__main__":
    app.run(debug=True)