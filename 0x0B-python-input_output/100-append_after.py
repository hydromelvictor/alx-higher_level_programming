#!/usr/bin/python3
"""append after
"""


def append_after(filename="", search_string="", new_string=""):
    """ filename: name of file
        search_string: string
        new_string: string  new
    """
    lineof = []
    with open(filename, "r", encoding="utf-8") as file:

        while True:
            line = file.readline()

            if line == "":
                break

            lineof.append(line)
            if search_string in line:
                lineof.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lineof)
