#!/usr/bin/python3
"""This module contains the defination
of User class that inherits from BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Here we define
    body to the class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
