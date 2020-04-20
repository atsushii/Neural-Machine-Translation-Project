# coding=utf-8
import unittest
from ...utils.preprocessing import Preprocess


class TestPreprocess(unittest.TestCase):
    def test_accent(self):
        preprocess = Preprocess("")
        assert preprocess.english_unicode_to_ascii(text="â") == "a"

    def test_upper_case(self):
        preprocess = Preprocess("")
        assert preprocess.english_unicode_to_ascii(text="HELLO") == "hello"

    def test_special_character(self):
        preprocess = Preprocess("")
        assert preprocess.replace_special_character_to_space_en(
            text="hello @^$") == "hello"

    def test_number(self):
        preprocess = Preprocess("")
        assert preprocess.replace_special_character_to_space_en(
            text="hello 123") == "hello"

    def test_space(self):
        preprocess = Preprocess("")
        assert preprocess.replace_special_character_to_space_en(
            text="hello!?") == "hello ! ?"

    def test_strip(self):
        preprocess = Preprocess("")
        assert preprocess.replace_special_character_to_space_en(
            text=" hello ") == "hello"

    def test_add_position_word(self):
        preprocess = Preprocess("hello")
        assert preprocess.normalize() == "start_ hello _end"
