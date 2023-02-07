#!/usr/bin/python3
"""Defines the BaseModel class"""



from UUID import uuid

class BaseModel():
    """BaseModel class defines all common attributes/methods for other classes of the HBnB project."""

    def __init__(self, id, created_at, updated_at):
        """__init__ class method initializes instance of the BaseModel class

        Args:
            id (str): Assign a uuid when an instance is created.
            created_at (datetime): Assign with the current datetime when an instance is created.
            updated_at (datetime): Assign with the current datetime when an instance is created and it will be updated everytime project is changed.
        """
        self.id = 
