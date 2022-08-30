'''
Test file for the 'BaseModel' class
'''

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.Testcase):
	'''
	TestBaseModel test class:
	contains the functions:
		-> test_basic 
		-> test_to_dict
		-> test_save
	'''
	def test_basic(self):
		base1 = BaseModel()
		self.assertRaises(AttributeError, )

if __name__ == '__main__':
	unittest.main()
