#!/usr/bin/python3
"""Defines the BaseModel class"""


from uuid import uuid4
from datetime import datetime

class BaseModel():
    """BaseModel class defines all common attributes/methods for other classes of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """__init__ class method initializes instance of the BaseModel class

        Args:
            id (str): Assign a uuid when an instance is created.
            created_at (datetime): Assign with the current datetime when an instance is created.
            updated_at (datetime): Assign with the current datetime when an instance is created and it will be updated everytime project is changed.
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """__str__ method that prints a string representation of BaseModel class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save method updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict method returns a dictionary containing all keys/values of __dict__ of the instance"""
        base_model_dict = self.__dict__
        base_model_dict["__class__"] = __class__.__name__
        base_model_dict["updated_at"] = self.updated_at.isoformat()
        base_model_dict["created_at"] = self.created_at.isoformat()

        return base_model_dict

