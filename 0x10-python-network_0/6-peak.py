#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """list_of_integers: list -> int
    return: int
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 2:
        return max(len_of_integers)

    n = len(list_of_integers) // 2
    peak = list_of_integers[n]
    
    if peak > list_of_integers[n - 1] and peak > list_of_integers[n + 1]:
        return peak
    elif peak < list_of_integers[n - 1]:
        return find_peak(list_of_integers[:n]
    else:
        return find_peak(list_of_integers[n + 1:]

