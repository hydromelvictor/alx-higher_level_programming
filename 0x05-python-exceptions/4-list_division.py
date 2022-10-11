#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    j = 0
    for i in range(list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except TypeError:
            print("wrong type")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            my_list.append(j)
    return my_list
