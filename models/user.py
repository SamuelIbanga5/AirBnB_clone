#!/usr/bin/python3
"""Defines the User class for user models"""


from models.base_model import BaseModel

class User(BaseModel):
    """User class defines the user model."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""