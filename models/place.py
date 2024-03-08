#!/usr/bin/python3

"""Module defining the Place class that inherits from BaseModel."""

from base_model import BaseModel

class Place(BaseModel):
    """
    A class representing Place, inheriting attributes from BaseModel.
    
    Public class attributes:
        - city_id: str - The ID of the City where the Place is located.
        - user_id: str - The ID of the User who owns the Place.
        - name: str - The name of the Place.
        - description: str - A description of the Place.
        - number_rooms: int - The number of rooms in the Place.
        - number_bathrooms: int - The number of bathrooms in the Place.
        - max_guest: int - The maximum number of guests allowed in the Place.
        - price_by_night: int - The price per night for the Place.
        - latitude: float - The latitude coordinate of the Place.
        - longitude: float - The longitude coordinate of the Place.
        - amenity_ids: list of str - A list of IDs of amenities associated with the Place.
    """

    def __init__(self):
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
