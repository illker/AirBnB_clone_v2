#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage():
    """that serializes instances to a JSON"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_ob, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as burger:
                beer = json.load(burger)
            for malta in beer:
                self.__objects[malta] = classes[beer[malta]["__class__"]](
                    **beer[malta])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if its inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
