from flask import Flask, request, render_template
from load_token_dic import load_english_dic, load_japanese_dic
from utils.text_preprocess import normalize_english
from utils.dataset import tokenize
from utils.model import Predict, CreateModel
import tensorflow as tf

# define model
model = tf.keras.models.load_model("saver/model/model.h1.22_Nov_19")

# create model
# load word token dic
english_tokens = load_english_dic()
japanese_tokens = load_japanese_dic()
model_ = CreateModel(model)

encoder, decoder = model_()

predict = Predict(encoder, decoder, japanese_tokens)

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
        normalize_lang = normalize_english(input_lang)
        # create input value for encode
        encoder_lang = tokenize(normalize_lang, english_tokens)

        # predict
        result["predict"] = predict.result(encoder_lang)

        return render_template("translate.html", lang=result)


if __name__ == "__main__":
    app.run(debug=True)