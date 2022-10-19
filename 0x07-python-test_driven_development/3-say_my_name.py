#!/usr/bin/python3

"""
    function say_my_name programming
"""


def say_my_name(first_name, last_name=""):
    """
        print the all name
        first_name: str
        last_name: str
        return str (My name is fisrt_name last_name)
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
