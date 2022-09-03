#!/usr/bin/python3
'''Module containing the definition of the 'City' class
'''
from models.base_model import BaseModel


class City(BaseModel):
    ''''City' class. Represents the details of a city in the real world

    Attributes:
        state_id (string): The ID (State.id) of an instance of class 'State'
        name (string): The name of the city.
    '''
    state_id = ""
    name = ""
