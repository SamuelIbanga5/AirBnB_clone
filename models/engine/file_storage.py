#!/usr/bin/python3
"""Defines the FileStorage class"""


import json

class FileStorage:
    """FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """all method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new method sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj['id']] = obj

    def save(self):
        """save method serializes __objects to the JSON file(path: __file_path)"""
        json_objects = json.dumps(self.__objects)
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            f.write(json_objects)




