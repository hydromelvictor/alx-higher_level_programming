#!/usr/bin/python3
"""class base
"""

import json


class Base:
    """base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """id: id for init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json
        """
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file json
        """
        filename = cls.__name__ + ".json"
        
        if list_objs is None:
            list_objs = []

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """deserialization of json_string 
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating functions
        """
        pass


