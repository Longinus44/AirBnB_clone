#!/usr/bin/python3

"""Module defining the Review class that inherits from BaseModel."""

from base_model import BaseModel

class Review(BaseModel):
    """ A class representing a Review, inheriting attributes from BaseModel.

    Public class attributes:
        - place_id: str - The ID of the City where the Place is located.
        - user_id: str - The ID of the User who owns the Place.
        - text: str - 
    """

    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""