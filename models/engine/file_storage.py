#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path:JSON file path
        __objects: objects to be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dict of all objects or objects of a specific
        class if cls is specified.
        Args:
            cls: objects Class type to be filtered
        Returns:
            Dictionary of objects or filtered objects by class
        """
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, BaseModel):
                cls_dict = {key: val for key,
                            val in self.__objects.items() if isinstance(val, cls)}
                return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dict.
        Args:
            obj: Object to be added
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serialize the file path to JSON file path and saves
        """
        with open(FileStorage.__file_path, 'w') as f:
            my_dict = {}
            my_dict.update(FileStorage.__objects)
            for key, value in my_dict.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to retrieve stored objects.
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            my_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj is None:
            return
        obj_to_del = f"{obj.__class__.__name__}.{obj.id}"

        try:
            del FileStorage.__objects[obj_to_del]
        except AttributeError:
            pass
        except KeyboardInterrupt:
            pass

    def close(self):
        """
        Reloads objects from the file, and closes the storage.
        """
        self.reload()
