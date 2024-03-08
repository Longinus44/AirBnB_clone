#!/usr/bin/python3

"""Module defining the City class that inherits from BaseModel."""

from base_model import BaseModel

class City(BaseModel):
    """
    A class representing a City, inheriting attributes from BaseModel.

    Public class attributes:
        - name: str - The name of the city.
        - id: str  - The id of the city
    """
    def __init__(self):
        super().__init__()
        self.state_id = ""
        self.name = ""
