import tensorflow as tf
import unicodedata
import re


class Preprocess():

    def __init__(self, text):
        self.text = text

    def english_unicode_to_ascii(self, text):
        """
        Normalize letter, removing an accented characters

        text: Str, input english text
        return: Engish text
        """
        text = text.lower()

        return ''.join(ascii_text for ascii_text in unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore'))

    def replace_special_character_to_space_en(self, text):
        """
        Remove special characters and create space between word and punc

        text: Str, input english text
        return: English text
        """
        text = re.sub(r"([?.!,¿])", r" \1 ", text)
        text = re.sub(r'[" "]+', " ", text)

        text = re.sub(r"[^a-zA-Z?.!,¿]+", " ", text)

        text = text.strip()

        return text

    def normalize(self):
        """
        Preprocess input text

        text: Str, input english text
        return: crean text
        """

        text = self.english_unicode_to_ascii(self.text)
        text = self.replace_special_character_to_space_en(text)

        text = "start_ " + text + " _end"

        return text
