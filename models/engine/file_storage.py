#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This is the class to help serialize an
    deserialize objects from JSON
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets  `in __objects the obj with key <obj class name>.id
        """
        check = "{}.{}".format(obj.__class__.__name__, obj.id)
        dict = {check : obj}
        self.__objects.update(dict)

    def save(self):
        """T o save to JSON format
        """
        with open (self.__file_path, "w") as fpoint:
            json.dump({k: v.to_dict() for k ,v in self.__objects.items()}, fpoint)

    def reload(self):
        """To deserialize JSON objects
        """
        try:
            with open(self.__file_path, "r") as rpoint:
                dict = json.loads(rpoint.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
