import unittest
import json
from src.utils.validation_data import Validation
from src.contants import MAX_LEN_TARGET, MAX_LEN_INPUT, UNITS, INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM, DROPOUT_RATE, BATCH_SIZE, OPTIMIZER
from src.utils.model import Model


class TestValidation(unittest.TestCase):

    def test_validation(self):

        model = Model(INP_VOCAB, TAR_VOCAB, EMBEDDING_DIM,
                      UNITS, BATCH_SIZE, DROPOUT_RATE, OPTIMIZER)
        _, _, input_token, _ = model.define_model()

        validation = Validation({
            "input": "hello"
        }, input_token)

        is_exist_key_validation = Validation({
            "English": "hello"
        }, input_token)

        is_exist_token_validation = Validation({
            "English": "hello @12e2"
        }, input_token)

        self.assertTrue(validation.valdation_data())
        self.assertFalse(is_exist_key_validation.valdation_data())
        self.assertFalse(is_exist_token_validation.valdation_data())
