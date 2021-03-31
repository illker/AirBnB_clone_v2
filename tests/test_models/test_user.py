#!/usr/bin/python3
""" test description for function """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import os


@unittest.skipIf((os.getenv("HBNB_TYPE_STORAGE") == "db"),
                 "Reason usage of DBStorage")
class test_User(test_basemodel):
    """ test description for function """

    def __init__(self, *args, **kwargs):
        """ test description for function """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.password), str)

if __name__ == "__main__":
    unittest.main()
