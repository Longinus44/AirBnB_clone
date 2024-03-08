#!/usr/bin/python3

"""Module defining the Amenity class that inherits from BaseModel."""

from base_model import BaseModel

class Amenity(BaseModel):
    """
    A class representing an Amenity, inheriting attributes from BaseModel.

    Public class attributes:
        - name: str - The name of the Amenity.
    """
    def __init__(self):
        super().__init__()
        self.name = ""
