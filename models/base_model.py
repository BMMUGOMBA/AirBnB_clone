#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ Defines all common attributes and methods for other classes that inherits from the class """
    def __init__(self, *args, **kwargs):
        """ initialization of class instance attributes """
        if kwargs:
            date_time = "%Y-%m-%dT%H:%M:%S.%f"
            arg_dict = kwargs.copy()
            del arg_dict["__class__"]
            for key in arg_dict:
                if (key == "created_at" or key == "updated_at"):
                    arg_dict[key] = datetime.strptime(arg_dict[key], date_time)
            self.__dict__ = arg_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    

    

    def to_dict(self):
        """ Generate a new dict with an extra field __class__ """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


    def save(self):
        """ Updates update_at """
        self.updated_at = datetime.today()
        storage.save()

    
    def __str__(self):
        """ Prints object in friendly format starting with class name followed by id and otehr attributes"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)