#!/usr/bin/python3
def search_replace(my_list, search, replace):
    str = []
    for i in my_list:
        if i == search:
            str.append(replace)
        else:
            str.append(i)
    return str
