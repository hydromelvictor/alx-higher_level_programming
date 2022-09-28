#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    str = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            str.append(key)
    for i in str:
        del a_dictionary[i]
    return a_dictionary
