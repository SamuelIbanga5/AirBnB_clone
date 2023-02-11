#!/usr/bin/python3
"""Defines the FileStorage class"""


import json
import sys
# sys.path.append(sys.path[0].replace("\models\engine", ""))
# print(sys.path)
# sys.path.append("...")

class FileStorage:
    """FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new method sets in __objects the obj with key <obj class name>.id"""
        if obj:
            self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """save method serializes __objects to the JSON file(path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """reload method deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                for obj in json.load(f).values():
                    self.new(eval(obj['__class__'])(**obj))
        except FileNotFoundError:
            return