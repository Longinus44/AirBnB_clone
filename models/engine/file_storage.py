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
            pass
