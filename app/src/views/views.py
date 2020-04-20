from flask import request, jsonify, Blueprint
import tensorflow as tf
from ..contants import MAX_LEN_TARGET, MAX_LEN_INPUT, UNITS, INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM, DROPOUT_RATE, BATCH_SIZE, OPTIMIZER
from ..model import Encoder, Decoder
from ..utils.model import Model
from ..utils.predict import Predict
from ..utils.preprocessing import Preprocess
from ..utils.validation_data import Validation

view_blueprint = Blueprint("view_blueprint", __name__)


@view_blueprint.route("/translate", methods=["GET"])
def translate():

    if request.method == "GET":
        data = request.get_json(force=True)

        # initialize model
        model = Model(INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM,
                      UNITS, BATCH_SIZE, DROPOUT_RATE, OPTIMIZER)
        encoder, decoder, input_token, target_token = model.define_model()

        # validation input data
        validation = Validation(data, input_token)

        if not validation.valdation_data():
            return jsonify({"status": 400,
                            "response": "Bad request"})

        data = data["input"]

        # predict
        predict = Predict(encoder, decoder, UNITS, MAX_LEN_INPUT,
                          MAX_LEN_TARGET, input_token, target_token, data)
        result, sentence = predict.predict()

    return jsonify({"status": 200,
                    "English": sentence,
                    "Japanese": result[:-4]})
