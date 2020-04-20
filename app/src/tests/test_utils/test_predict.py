import unittest
from ...utils.predict import Predict
from ...contants import MAX_LEN_TARGET, MAX_LEN_INPUT, UNITS, INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM, DROPOUT_RATE, BATCH_SIZE, OPTIMIZER
from ...utils.model import Model


class TestPredict(unittest.TestCase):
    def test_predict_value(self):
        input_text = "Hello"
        model = Model(INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM,
                      UNITS, BATCH_SIZE, DROPOUT_RATE, OPTIMIZER)

        encoder, decoder, input_token, target_token = model.define_model()

        predict = Predict(encoder, decoder, UNITS, MAX_LEN_INPUT,
                          MAX_LEN_TARGET, input_token, target_token, input_text)

        self.assertEqual((predict.predict()), ("こんにちは_end", "Hello"))
