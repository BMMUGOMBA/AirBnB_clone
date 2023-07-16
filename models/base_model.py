#!/usr/bin/python3
#  a class BaseModel that defines all common attributes/methods for other classes

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        #self.created_at = datetime.now()
        #self.updated_at = self.created_at
        
        now = datetime.now()
    
        self.created_at = now
        self.updated_at = now


    def __str__(self):
        
        # Get the name of the class of the object
        class_name = type(self).__name__
        # Get the id of the object
        id = self.id
        # Get the dictionary of attributes of the object
        attributes = self.__dict__
        # Return a formatted string that contains the class name, id, and attributes of the object
        return f"[{class_name}] ({id}) {attributes}"
        #return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.now()


    def to_dict(self):
        obj_ct = self.__dict__.copy()
        obj_ct['__class__'] = self.__class__.__name__
        obj_ct['created_at'] = self.created_at.isoformat()
        obj_ct['updated_at'] = self.updated_at.isoformat()
        return obj_ct
