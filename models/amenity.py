#!/usr/bin/python3
'''Definition of Amenity class
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity: class defines attributes that describe amenities
    available at specified locations

    Attributes:
        name (string): Amenity name
    '''
    name = ""
