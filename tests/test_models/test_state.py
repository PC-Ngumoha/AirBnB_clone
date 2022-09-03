'''Test file for the 'State' class definition.
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    ''''TestState' class. Used to test the definition of the 'State' class.
    '''
    def setUp(self):
        '''Sets up variables for use in later parts of the test.
        '''
        self.state1 = State()
        self.state1.save()

    def test_inherit_from_BaseModel(self):
        '''test if the instance of class 'State' inherits from 'BaseModel'
        '''
        self.assertIsInstance(self.state1, BaseModel)

    def test_hasattr_name(self):
        '''test if the 'State' class instance has the 'name' class attribute
        '''
        self.assertTrue(hasattr(self.state1, "name"))


if __name__ == '__main__':
    unittest.main()
