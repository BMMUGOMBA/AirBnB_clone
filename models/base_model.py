import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)


    def __str__(self):
        #return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        # Get the name of the class of the object
        class_name = type(self).__name__
        # Get the id of the object
        id = self.id
        # Get the dictionary of attributes of the object
        attributes = self.__dict__
        # Return a formatted string that contains the class name, id, and attributes of the object
        return f"[{class_name}] ({id}) {attributes}"


    def save(self):
        self.updated_at = datetime.now()


    def to_dict(self):
        obj_ct = self.__dict__.copy()
        obj_ct['__class__'] = self.__class__.__name__
        obj_ct['created_at'] = self.created_at.isoformat()
        obj_ct['updated_at'] = self.updated_at.isoformat()
        return obj_ct
