#!/usr/bin/python3



class FileStorage:
    """This is the class to help serialize an
    deserialize objects from JSON
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        dict1 = self.__objects
        return ()

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        check = "{}.{}".format(obj.__class__, obj.id)
        dict = {check : obj}
        self.__objects.update(dict)

    def save(self):
        """T o save to JSON format
        """
        with open (self.__file_path, "w") as fpoint:
            json.dump(self.__object, fpoint)

    def reload(self):
        """To deserialize JSON objects
        """
        with open(self.__file_path, "r") as rpoint:
            readfile = rpoint.read()
        return (readfile)
