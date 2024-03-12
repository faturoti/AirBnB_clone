#!/usr/bin/python3
"""
The module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Custom amenity class

    Attributes:
        name(str): The amenity name
    """
    name = ""
