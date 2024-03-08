<<<<<<< HEAD
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
=======
#!/usr/bin/python3

import os
import json
from base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

    Private class attributes:
        - __file_path: str - The path to the JSON file.
        - __objects: dict - Dictionary to store all serialized objects.

    Methods:
        - all(self): Returns the dictionary __objects.
        - new(self, obj): Sets in __objects the obj with key <obj class name>.id.
        - save(self): Serializes __objects to the JSON file.
        - reload(self): Deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary containing all serialized objects.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            - obj: object - The object to be serialized.
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""

        serialized = {}
        for key, value in FileStorage.__objects.keys():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised).
        """

        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance

        except FileNotFoundError:
>>>>>>> d2d4d39c8750e7f1c37fd8bb31bce659406dd79f
            pass
