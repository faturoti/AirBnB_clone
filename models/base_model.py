#!/usr/bin/python3
import uuid
from datetime import datetime
import json
import models


"""Define a BaseModel class to be inherited by other classes"""


class BaseModel:
    """Represent a BaseModel
    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4());
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        

        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, DATE_TIME_FORMAT)
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, DATE_TIME_FORMAT)
    
    def __str__(self):
        """Return the string representation of the Rectangle.
        Represent the BaseModel in string format
        """
        dictionary1 = {'my_number' : 89, 'name' : 'My First Model'}
        dictionary1.update({'id' : self.__dict__['id']})
        dictionary1.update({'updated_at' : self.__dict__['updated_at'].isoformat()})
        dictionary1.update({'created_at' : self.__dict__['created_at'].isoformat()})
        rect = "[Basemodel] ({}) {}".format(self.id, dictionary1)
        return (rect)
    
    def save(self):
        """ updates the public instance attribute updated_at 
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        return

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
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary1[key] = value.isoformat()
            else:
                dictionary1[key] = value
        return (dictionary1) 
