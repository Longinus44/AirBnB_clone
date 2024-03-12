#!/usr/bin/pyhton3

'''Module ccan serialize and deserialize to and from JSON file.'''
import json


class FileStorage():
    '''Class handles readinf and saving to json string format.'''
    
    def  __init__(self):
        '''Initialise private attriubutes.'''

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''Method displays all instaces created so far.'''

        if self.reload():
            return self.reload()
        else:
            return {}

    def new(self, obj):
        ''''Sets class atribute __object.'''

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.__dict__
        return self.__objects

    def save(self):
        '''Method serializes and saves to json string format'''

        new_objects = self.all()
        for key in self.__objects:
            new_objects[key] = self.__objects[key]
            #print(new_objects)
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(new_objects, default=str))

    def reload(self):
        '''Method deserializes a string into object.'''
            
        try:
            with open(self.__file_path, 'r') as f:
                data =  f.read()
                return json.loads(data)

        except FileNotFoundError:
            pass
