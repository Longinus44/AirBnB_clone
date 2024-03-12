#!/usr/bin/python3

from models.base_model import BaseModel

"""Module defining the User class that inherits from BaseModel."""

class User(BaseModel):
    """
    A class representing User, inheriting attributes from BaseModel.

    Public class attributes:
        - email: str - The email of the User.
	- password: str - The password of the User.
	- first_name: str - The first-name of the User.
	- last_name: str - The last-name of the User.
    """
    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
 
