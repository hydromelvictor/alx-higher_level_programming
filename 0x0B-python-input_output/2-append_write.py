#!/usr/bin/python3
"""add an word in the file
"""


def append_write(filename="", text=""):
    """ filename: name of file
        text: word from file
    """
    with open(filename, 'w+', encoding="utf-8") as file:
        return file.write(text)