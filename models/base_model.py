#!/usr/bin/python3
'''Base class from whom all inherit.'''
import datetime
import uuid
from models.__init__ import storage
from models.__init__ import storage


class BaseModel():
    '''Calss defines all common attributes/methods for child classes.'''

    def __init__(self, *args, **kwargs):
        '''Initialize private instace attributes.'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
                    #print(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        '''Method updates `updated_at with current datetime.'''

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        '''Method returns dictionary of all key/values of __dict__ of instance'''

        self.__dict__["__class__"] = __class__.__name__
        self.created_at.isoformat()
        self.updated_at.isoformat()
        self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__


    def __str__(self):
        '''Print  string representation of object.'''

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
