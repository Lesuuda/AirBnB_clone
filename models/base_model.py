#!/usr/bin/python3
"""
class BaseModel that defines all commmon attributes/
methods for other classes
"""


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    base class that defines all common attributes/methods
    for other classes
    """


    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        it represents class object as strings
        """
        return "([{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """
         updates the public instance attribute
         updated_at with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance:
        """
        dictionary = {**self.__dict__}
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

    
