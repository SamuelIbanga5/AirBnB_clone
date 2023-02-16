#!/usr/bin/python3
"""Defines the FileStorage class"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new method sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]\
            = obj

    def save(self):
        """save method serializes __objects to the JSON file
        (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """reload method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;"""
        dct = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "Amenity": Amenity
        }

        try:
            with open(self.__file_path, encoding='utf-8') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value["__class__"]](**value))
        except FileNotFoundError:
            return
