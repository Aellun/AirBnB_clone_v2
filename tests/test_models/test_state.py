#!/usr/bin/python3
""" unit test for the class place module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """initialization of class  """

    def __init__(self, *args, **kwargs):
        """ arguments"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """name """
        new = self.value()
        self.assertEqual(type(new.name), str)
