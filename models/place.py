#!/usr/bin/python3
'''Definition of Place class
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Place: Defines data describing locations, it inherits from
    BaseModel

    Attributes:
        city_id (string): Unique id of place object
        user_id (string): Unique id of useer
        name (string): The name of location being described
        description (string): Short description of location object
        number_rooms (int): Defines the number of rooms
        number_bathrooms (int): Defines the number of bathrooms present
        max_guests (int): Defines maximum number of guests location can hold
        price_by_night (int): Defines the price per night of current location
        latitude (float): The latitudinal position of loacation
        longitude (float): The longitudinal position of loacation
        amenity_ids (list): List of amenities present at location
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
