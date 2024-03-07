#!/usr/bin/python3
import uuid
from datetime import datetime
import json


"""Define a BaseModel class to be inherited by other classes"""


class BaseModel:

    """Represent a BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4());
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())
    
    def __str__(self):
        """Return the string representation of the Rectangle.
        Represent the BaseModel in string format
        """
        dictionary1 = {'my_number' : 89, 'name' : 'My First Model'}
        dictionary1.update(self.__dict__)
        rect = "[Basemodel] ({}) {}".format(self.id, dictionary1)
        return (rect)
    
    def save(self):
        """ updates the public instance attribute updated_at 
        with the current datetime
        """
        updated_at = str(datetime.now())

    def merge():
        """To merge two dictionaries
        It maerges dict2 to dict1 to produce another object
        """
        dictionary1 = {'my_number' : 89, 'name' : 'My First Model'}
        dictionary1.update(self.__dict__)
        return (dictionary1)

    def to_dict(self):
        """returns a dictionary containing all keys/values 
        of __dict__"""
        dictionary1 = {'my_number' : 89, 'name' : 'My First Model'}
        dictionary1.update(self.__dict__)
        with open("mydata.txt", "w") as fpoint:
            json.dump(dictionary1, fpoint)
        return (dictionary1) 
