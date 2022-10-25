#!/usr/bin/python3
"""writen in the file
"""


def write_file(filename="", text=""):
    """ filename: name of file
        text: word from file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
