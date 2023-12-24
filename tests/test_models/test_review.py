#!/usr/bin/python3
"""review class odule unit test """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """reviewclass test cases """

    def __init__(self, *args, **kwargs):
        """ review class instance initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ id test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
