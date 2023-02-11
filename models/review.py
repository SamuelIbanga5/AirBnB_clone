#!/usr/bin/python3
"""Defines Review class inheriting from BaseModel"""


from models.base_model import BaseModel

class Review(BaseModel):
    """Defines Review class inheriting BaseModel attributes"""
    place_id = ""
    user_id = ""
    text = ""