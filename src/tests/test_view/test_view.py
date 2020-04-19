import unittest
import json
from src import app
from src.views import views
from src.contants import UNITS, INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM, DROPOUT_RATE, BATCH_SIZE, OPTIMIZER
from src.utils.model import Model
import json


class TestView(unittest.TestCase):

    def test_correct_value(self):
        client = app.test_client()
        url = "/translate"

        input_data = {
            "input": "hello"
        }

        response = client.get(url, data=json.dumps(input_data))

        data = json.loads(response.get_data().decode("utf8"))
        assert response.status_code == 200
        assert data["status"] == 200

    def test_incorrect_value(self):
        client = app.test_client()
        url = "/translate"

        input_data = {
            "input": "コンにちは"
        }

        response = client.get(url, data=json.dumps(input_data))
        data = json.loads(response.get_data().decode("utf8"))
        assert response.status_code == 200
        assert data["status"] == 400

    def test_incorrect_key(self):
        client = app.test_client()
        url = "/translate"

        input_data = {
            "English": "hello"
        }

        response = client.get(url, data=json.dumps(input_data))
        data = json.loads(response.get_data().decode("utf8"))
        assert response.status_code == 200
        assert data["status"] == 400

    def test_vprediction(self):
        input_text = "hello"
        model = Model(INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM,
                      UNITS, BATCH_SIZE, DROPOUT_RATE, OPTIMIZER)

        encoder, decoder, input_token, target_token = model.define_model()

        result, sentence = views.prediction(encoder, decoder,
                                            input_token, target_token, input_text)

        self.assertEqual((result, sentence), ("こんにちは_end", "hello"))
