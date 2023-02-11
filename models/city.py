#!/usr/bin/python3
"""Defines City class that inherits from BaseModel"""


from models.base_model import BaseModel

class City(BaseModel):
    """City class defines city model inheriting BaseModel attributes"""
    state_id = ""
    name = ""
    