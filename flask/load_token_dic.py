import json


def load_english_dic():
    """
    load english token json for tokenize input
    :return: english dict
    """

    with open("english_dict", "r") as f:
        return json.load(f)


def load_japanese_dic():
    """
    load japanese token json for predict
    :return: japanese dict
    """

    with open("japanese_word.json", "r") as f:
        return json.load(f)

