'''Tests the code definition of the 'City' class.
'''
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    ''''TestCity' class. Tests the definition of the 'City' class.
    '''
    def setUp(self):
        '''sets up the variables for use in later tests.
        '''
        self.city1 = City()
        self.city1.save()

    def test_inherit_BaseModel(self):
        '''Tests if the instance of 'City' class inherits from 'BaseModel'
        '''
        self.assertIsInstance(self.city1, BaseModel)

    def test_hasattr_name(self):
        '''Tests if the instance of 'City' class has 'name' class attribute
        '''
        self.assertTrue(hasattr(self.city1, "name"))

    def test_hasattr_state_id(self):
        '''Tests if the instance of 'City' class has 'state_id' class attribute
        '''
        self.assertTrue(hasattr(self.city1, "state_id"))


if __name__ == '__main__':
    unittest.main()
