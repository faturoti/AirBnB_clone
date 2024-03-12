#!/usr/bin/python3

"""Test file for Base Model class
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """
    def setUp(self):
        """
        Set up function for unit test
        """
        pass

    def test_basic(self):
        """
        Test for basic stuff
        """
        my_model = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_datetime(self):
        """
        Test for created and updated time
        """
        mymodel1 = BaseModel()
        self.assertNotEqual(mymodel1.created_at, mymodel1.updated_at)
