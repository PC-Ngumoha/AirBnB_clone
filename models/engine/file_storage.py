#!/usr/bin/python3
'''Module contains 'FileStorage' class definition.
'''
import json
import base_model


class FileStorage:
    '''class FileStorage.
    Handles persitence for the application by saving objects to the file
    'file.json'
    '''
    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        '''Returns the contents of the '__objects' dictionary
        '''
        return __objects

    def new(self, obj):
        '''Adds the object 'obj' to the collection of objects in the
        '__objects' dictionary.
        '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        __objects[key] = obj.to_dict()

    def save(self):
        '''Saves the contents of the '__objects' dictionary to the json file
        specified in the '__file_path' class attribute.
        '''
        with open(__file_path, 'w', encoding='utf-8') as fp:
            json.dump(__objects, fp)

    def reload(self):
        '''Sets the '__objects' dictionary with the collection of objects
        retrieved for the file.json file.
        '''
        try:
            with open(__file_path, 'r', encoding='utf-8') as fp:
                __objects = json.load(fp)
        except IOError:
            pass
