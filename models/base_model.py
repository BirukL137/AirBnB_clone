#!/usr/bin/python3
"""Contains class defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """defines common attributes/methods for other classes"""
    def __init__(self):
        """initialize attributes of BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """modified string representation of object"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates public instance attr 'updated_at' with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the __dict__
        instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

