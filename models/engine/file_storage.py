#!/usr/bin/python3
"""This is a class Filestorage that handle
Json to file and from file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


class FileStorage:
    """This is body of the
    File Storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns
        the dictionary __objects
        """
        return self.__class__.__objects

    def new(self, obj):
        """This method sets in
        __objects
        """
        m = obj.__class__
        s = self.__class__
        key = "{}.{}".format(m.__name__, obj.id)
        s.__objects[key] = obj

    def save(self):
        """This method serializes
        __objects to the Json
        """
        m = self.__class__
        my_dict = m.__objects.copy()
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        with open(m.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(my_dict))

    def reload(self):
        """This method deserializes
        for Json string file
        """
        m = self.__class__
        try:
            with open(m.__file_path, 'r', encoding='utf-8') as f:
                my_dict = json.loads(f.read())
                for values in my_dict.values():
                    name = values['__class__']
                    self.new(eval(name)(**values))
        except FileNotFoundError:
            pass
