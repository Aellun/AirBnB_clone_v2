#!/usr/bin/python3
"""unit test for the class user module """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test cases for the class user"""

    def __init__(self, *args, **kwargs):
        """ instances initilization"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
