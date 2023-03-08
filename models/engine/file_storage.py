#!/usr/bin/python3
"""This is a class Filestorage that handle
Json to file and from file
"""
import json


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
        s.__objects[key] = obj.to_dict()

    def save(self):
        """This method serializes
        __objects to the Json
        """
        m = self.__class__
        with open(m.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(m.__objects))

    def reload(self):
        """This method deserializes
        for Json string file
        """
        m = self.__class__
        try:
            with open(m.__file_path, 'r', encoding='utf-8') as f:
                m.__objects = json.loads(f.read())
        except Exception:
            pass
