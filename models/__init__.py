#!/usr/bin/python3
"""This is __init__.py
method
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
