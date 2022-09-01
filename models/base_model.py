#!/usr/bin/python3
'''
Defines BaseModel as super class for all aother classes in AirBnB Project
'''
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    '''
    BaseModel provides all methods and attributes for
    subclasses in the AirBnb project.

    Attributes:
        id (string): Assigned as a unique identifier for
            each instance of BaseModel created using uuid4().
        created_at (datetime): A Datetime object assigned to BaseModels
            when instances are created.
        updated_at (datetime): A datetime object assigned to each instance
            of BaseModel at initialization, and is reset when save() is called.
    '''
    def __init__(self, *args, **kwargs):
        '''Initialization method, called each time an instance is created.
        If kwargs is not empty, an new instance is created from the key/value
        pairs found in kwargs, otherwise a completely new object is created

        Args:
            *args: Variable length argument list.
                It is not used when new object is initialized.
            **kwargs: Arbitrary kewword arguments. With the following expected:
                id, created_at, updated_at.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''Method to set the string representation of BaseModel object.

        Return:
            The string representation returned follows the following format:
            [<class name>] (<self.id>) <self.__dict__>
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Updates the public attribute `updated_at` with the current time
        '''
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        '''This method is used for serialization of object by returning the
        dictionary of the object with added key/value pairs(__class__).

        Return:
            A dictionary containing all the keys/value of __dict__ method
            of the instance. A key __class__ is added to this dictionary
            with the class name of the object
        '''
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result
