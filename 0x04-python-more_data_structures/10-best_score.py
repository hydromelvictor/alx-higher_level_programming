#!/usr/bin/python3
def best_score(a_dictionary):
    n = 0
    if a_dictionary:
        n = max([a_dictionary[key] for key in a_dictionary])
        for i in a_dictionary:
            if a_dictionary[i] == n:
                return i
