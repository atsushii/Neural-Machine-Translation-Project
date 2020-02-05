import config as cfg
import numpy as np


def tokenize(input_lang, english_dic):
    """
    convert input value to vector

    :param input_lang: String, English language
    :param english_dic: dictionary, tokenize dictionary
    :return: encoder input
    """

    # max length of input sentence
    english_len = len(input_lang.split())

    encoder_input_data = np.zeros((english_len, cfg.MAX_INPUT_SIZE), dtype="float32")

    # tokenize
    for i , word in enumerate(input_lang.split()):
        encoder_input_data[1, i] = english_dic[word]

    return encoder_input_data


