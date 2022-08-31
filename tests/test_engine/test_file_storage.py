#!/usr/bin/python3
'''Test file for FileStorage Class
'''
import unittest
import json
from models import storage
from models.base_models import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''TestFileStorage class built to test regular
    and edge case usage of FileStorage Class.
    Inherits from TestCase class in unittest module.
    '''

    def test_file_path_is_private_from_instance(self):
        '''Test to ensure `__file_path` class attribute is a
        private class attribute thus inaccessible when
        referenced through instances
        '''
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path

    def test_file_path_is_private_from_class(self):
        '''Test to ensure `__file_path` private class attribute is a
        private class attribute thus inaccessible when
        referenced through the class.
        '''
        with self.assertRaises(AttributeError):
            file_path = FileStorage.__file_path

    def test_file_path_type(self):
        '''Test fails if `__file_path` private class attribute is not of type
        str
        '''
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        '''Test fails if `__objects` private class attribute is not of type
        dict
        '''
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_all(self):
        '''Test ensures public instance method `all`
        returns private class attribute `__objects`
        '''
        self.assertEqual(
            storage.all(),
            storage._FileStorage__objects
        )

    def test_new(self):
        '''Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        executes accordingly.
        '''
        self.test_model_0 = BaseModel(
            id="12345678",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        storage.new(self.test_model_0)
        self.assertEqual(len(storage.all()), 1)

    def test_new_accurate(self):
        '''Tests to ensure that public instance method `new(obj)`
        intended to add obj to the private class attribute `__objects`
        stores the obj data accurately.
        '''
        self.assertEqual(
            storage.all()[
                f"{self.test_model_0.__class__.__name__}.id"
            ],
            self.test_model_0.to_dict()
        )

    def test_objects_key_format(self):
        '''Test the format of all items in the dict stored as
        `__objects` private class attribute to ensure all keys follow format:
        "<class name>.id"
        '''
        test_model_1 = BaseModel()
        test_model_2 = BaseModel()
        for key in storage.all().keys():
            self.assertEqual(
                key,
                f"{storage.all()[key].__class__.__name__}.id"
            )

    def test_objects_value_type(self):
        '''Test ensures all items in `__objects` private class
        attribute dictionary have values of type BaseModel.
        '''
        test_model_3 = BaseModel()
        test_model_4 = BaseModel()
        for value in storage.all().values():
            self.assertIsInstance(value, dict)

    def test_save(self):
        '''Tests the FileStorage public instance method `save()`
        intended to save the current value of private class
        attribute `__objects` to the file specified by `__file_path`
        '''
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            self.assertIsInstance(data, dict)
            self.assertEqual(data, storage.all())

    def test_reload(self):
        '''Tests the public instance method `reload` which deserializes
        the JSON in __file_path and assigns it to __objects
        '''
        prev_objs = storage.all()
        test_model_5 = BaseModel()  # The sixth item in `__objects`
        curr_objs = storage.all()
        storage.reload()
        self.asserNotEqual(storage.all(), curr_objs)
        self.assertEqual(storage.all(), prev_objs)


if __name__ == "__main__":
    unittest.main()
