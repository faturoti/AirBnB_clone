#!/usr/bin/python3

"""
Test suits for amenities
"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test for the User class for each user
    """
    def test_email(self):
        """Test equality of email"""
        user1 = User()
        user2 = User()
        self.assertEqual(user1.password, user2.first_name)
