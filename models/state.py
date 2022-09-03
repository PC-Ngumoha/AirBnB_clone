#!/usr/bin/python3
'''Module contains the definition of the class 'State'
'''
from models.base_model import BaseModel


class State(BaseModel):
    ''''State' class. Represents a state in the real world.

    Attributes:
        name (string): The name of the state.
    '''
    name = ""
