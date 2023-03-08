#!/usr/bin/python3
"""This module contains the defination of
BaseModel class
"""
from datetime import datetime
import uuid


class BaseModel:
    """This is body of the
    class
    """
    def __init__(self, *args, **kwargs):
        """This is the constructor of
        the class
        """
        if kwargs:
            for ky, value in kwargs.items():
                if ky == '__class__':
                    continue
                elif ky == 'created_at' or ky == 'updated_at':
                    self.__dict__[ky] = datetime.fromisoformat(value)
                else:
                    self.__dict__[ky] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """This is a magic
        string method
        """
        m = self.__class__.__name__
        return "[{}] ({}) {}".format(m, self.id, self.__dict__)

    def save(self):
        """This method is used to
        update the updated_at attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns
        dictionary
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
