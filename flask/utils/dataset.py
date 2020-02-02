import config as cfg
import numpy as np

def convert_to_nparray(input_lang):
    """
    convert input value to vector

    :param input_lang: String, English language
    :return: encoder input
    """

    # max length of input sentense
    english_len = len(input_lang.split())

    encoder_input_data = np.zeros((english_len, cfg.MAX_INPUT_SIZE), dtype="float32")

    # tokenize
    for i , word in enumerate(input_lang.split()):
        encoder_input_data[1, i] = token_dict[word]

    return encoder_input_data


