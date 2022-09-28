#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    ch = [i[0]*i[1] for i in my_list]
    n = [i[1] for i in my_list]
    return sum(ch) / sum(n)
