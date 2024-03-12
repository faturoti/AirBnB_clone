#!/usr/bin/python3
"""
Unit tests for console testing
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
"""StringIO not used"""
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test file for console"""
    def setUp(self):
        """This is to start up the console"""
        pass

    def test_quit(self):
        """Test Quit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

if __name__ == '__main__':
    unittest.main()
