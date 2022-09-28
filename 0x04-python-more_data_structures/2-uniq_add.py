#!/usr/bin/python3
def uniq_add(my_list=[]):
    str = []
    for i in my_list:
        if i not in str:
            str.append(i)
    return sum(str)
