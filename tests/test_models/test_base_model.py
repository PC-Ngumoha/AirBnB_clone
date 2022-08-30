'''
Test file for the 'BaseModel' class
'''

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.Testcase):
	'''
	TestBaseModel test class: contains the test functions
	Each test function represents a single test case.
	'''
	def test_if_public_attribute(self):
		'''
		tests if the 'id', 'created_at' and 'updated_at' instance attributes
		are public instance attributes.
		'''
		base1 = BaseModel()
		with self.assertRaises(AttributeError):
			try:
				unique_id = base1.id
				time_created = base1.created_at
				time_updated = base1.updated_at
			except:
				pass
			else:
				raise AttributeError

	def test_string_format(self):
		'''
		tests the format of the string representation of a 'BaseModel' object
		'''
		base1 = BaseModel()
		test_string = f"[{base1.__class__.__name__}] ({base1.id}) {base1.__dict__}"
		self.assertEqual(str(base1), test_string)

	def test_id_type(self):
		'''
		tests id's type to see if it's a string
		'''
		base1 = BaseModel()
		self.assertIs(type(base1.id), str)

if __name__ == '__main__':
	unittest.main()
