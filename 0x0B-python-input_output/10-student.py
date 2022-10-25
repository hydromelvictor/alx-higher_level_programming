#!/usr/bin/python3
""" student class
"""


class Student:
    """student class defined
    """
    def __init__(self, first_name, last_name, age):
        """ first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json
        """
        dict = []
        if attrs is None:
            return self.__dict__
        else:
            for a in attrs:
                dict.append(self.__dict__[a])
            return dict
