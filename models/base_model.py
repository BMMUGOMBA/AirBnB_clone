#!/usr/bin/python3
#  a class BaseModel that defines all common attributes/methods for other classes

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.now()


    def to_dict(self):
        obj_ct = self.__dict__.copy()
        obj_ct['__class__'] = self.__class__.__name__
        obj_ct['created_at'] = self.created_at.isoformat()
        obj_ct['updated_at'] = self.updated_at.isoformat()
        return obj_ct
