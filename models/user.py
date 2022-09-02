'''Definition of User class
'''
from base_model import BaseModel


class User(BaseModel):
    '''User: Defines data describing users, it inherits from BaseModel class

    Attributes:
        email (string): Email of user stored as a string.
        password (string): User password.
        first_name (string): Users first name.
        last_name (string): Users last name.
    '''
    def __init__(self):
        '''Defines steps to follow when object is initialized
        '''
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
