#!/usr/bin/python3
"""Defines User class inheriting from BaseModel"""


from models.base_model import BaseModel

class State(BaseModel):
    """State class defines state model with BaseModel attributes"""
    name = ""
    