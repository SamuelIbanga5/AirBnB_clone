#!/usr/bin/python3
"""Defines the BaseModel class"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class defines all common attributes/methods for other classes of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """__init__ class method initializes instance of the BaseModel class

        Args:
            id (str): Assign a uuid when an instance is created.
            created_at (datetime): Assign with the current datetime when an instance is created.
            updated_at (datetime): Assign with the current datetime when an instance is created and it will be updated everytime project is changed.
        """
        if len(kwargs) == 0:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            

    def __str__(self):
        """__str__ method that prints a string representation of BaseModel class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save method updates the public instance attribute updated_at with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict method returns a dictionary containing all keys/values of __dict__ of the instance"""
        base_model_dict = self.__dict__.copy()
        base_model_dict["__class__"] = __class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                base_model_dict[key] = value

        return base_model_dict

