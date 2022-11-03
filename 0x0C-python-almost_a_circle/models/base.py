#!/usr/bin/python3
"""class base
"""

import json
import os


class Base:
    """base class"""

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
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file json
        """
        filename = cls.__name__ + ".json"
        obj = cls.to_json_string(list_objs)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(obj)

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
        """creating functions"""
        return cls(4, 2, 1).update(dictionary)

    @classmethod
    def load_from_file(cls):
        """loads form file"""
        filename = cls.__name__ + ".json"

        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                for i in file:
                    cls.from_json_string(i)
        else:
            return []
