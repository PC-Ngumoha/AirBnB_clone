#!/usr/bin/python3
'''Definition of User class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User: Defines data describing users, it inherits from BaseModel class

    Attributes:
        email (string): Email of user stored as a string.
        password (string): User password.
        first_name (string): Users first name.
        last_name (string): Users last name.
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
