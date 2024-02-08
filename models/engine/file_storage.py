#!/usr/bin/pyhton3
"""
 class FileStorage that serializes instances to a JSON file and
 deserializes JSON file to instances
"""


import json
import os
from models.base_model import BaseModel



class FileStorage():
    """
     class FileStorage that serializes instances to a JSON file and
     deserializes JSON file to instances by first converting python dictionaries
     to strings and saving it to a JSON file. when deserializing,
     the JSON string is first converted to a python dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        private instantiation method with private attributes
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
                   by <class name>.id
        """

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {key: value.to_dict() for key, value in FileStorage.__objects.items()}, f)
        
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                file_content = f.read()
                if file_content:
                    try:
                        dict_obj = json.loads(file_content)
                        FileStorage.__objects = {key: BaseModel(**value) for key, value in dict_obj.items()}
                    except json.JSONDecodeError:
                        pass
                else:
                    print("there is no json file to decode")
        else:
            return