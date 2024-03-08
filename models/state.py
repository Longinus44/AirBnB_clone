#!/usr/bin/python3

"""Module defining the State class that inherits from BaseModel."""

from base_model import BaseModel


class State(BaseModel):
	"""
    A class representing a State, inheriting attributes from BaseModel.

    Public class attributes:
        - name: str - The name of the State.
    """
	def __init__(self):
		super().__init__()
		self.name = ""
