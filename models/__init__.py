#!/usr/bin/python3
"""This is __init__.py
method
"""
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
