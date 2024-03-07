#!/usr/bin/python3
'''Base class from whom all inherit.'''
import datetime
import uuid

class BaseModel():
    '''Calss defines all common attributes/methods for child classes.'''

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''Method updates `updated_at with current datetime.'''

        updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Method returns dictionary of all key/values of __dict__ of instance'''

        self.__dict__["__class__"] = __class__.__name__
        str(self.created_at)
        str(self.updated_at)
        return (self.__dict__)
    def __str__(self):
        '''Print  string representation of object.'''

        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))
