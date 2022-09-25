#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        str = []
        for i in my_list:
            if i % 2 == 0:
                str.append(True)
            else:
                str.append(False)
        return str
