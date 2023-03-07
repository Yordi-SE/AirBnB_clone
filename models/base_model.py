#!/usr/bin/python3
"""This module contains the defination of
BaseModel class
"""
import datetime
import uuid


class BaseModel:
    """This is body of the
    class
    """
    def __init__(self):
        """This is the constructor of
        the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """This is a magic
        string method
        """
        m = BaseModel.__name__
        return "[{}] ({}) {}".format(m, self.id, self.__dict__)

    def save(self):
        """This method is used to
        update the updated_at attribute
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method returns
        dictionary
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = BaseModel.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
