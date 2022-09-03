#!/usr/bin/python3
'''Definition of class Review
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review: Stores data for reviews

    Attributes:
        place_id (string): Unique id for Review objects
        user_id (string): id of user object who authored Review
        text (string): Text containing review message
    '''
    place_id = ""
    user_id = ""
    text = ""
