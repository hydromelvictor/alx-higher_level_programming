#!/usr/bin/python3
"""write in the file for json format
"""

import json


def save_to_json_file(my_obj, filename):
    """ my_obj: object
        filename: name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
