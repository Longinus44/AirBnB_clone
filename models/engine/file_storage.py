#!/usr/bin/pyhton3
'''Module ccan serialize and deserialize to and from JSON file.'''
import json


class FileStorage():
    '''Class handles readinf and saving to json file.'''

    def __init__(self):
        '''Initialize file name and object to store.'''

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''Mothod returns the directory object.'''

        if self.reload():
            return self.reload()
        else:
            return {}

    def new(self, obj):
        '''Sets class atribute __object.'''

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.__dict__
        return self.__objects

    def save(self):
        '''Method serializes and saves string to json file'''

        new_objects= self.all()
        for i in self.__objects:
            key = i
            break
        new_objects[key] = self.__objects[key]
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(new_objects, default=str))

    def reload(self):
        '''Method deserializes a string into object.'''
            
        try:
            with open(self.__file_path, 'r') as f:
                data =  f.read()
                return json.loads(data)

        except:
            pass
