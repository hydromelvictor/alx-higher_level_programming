#!/usr/bin/python3
"""append after
"""


def append_after(filename="", search_string="", new_string=""):
    """ filename: name of file
        search_string: string
        new_string: string  new
    """
    with open(filename, "r+", encoding="utf-8") as file:
        for line in file:
            if line == search_string:
                file.write(new_string)
