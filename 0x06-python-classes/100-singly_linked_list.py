#!/usr/bin/python3
"""struct data programming"""


class Node:
    """strcut data node"""
    def __init__(self, data, next_node=None):
        """init method"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node)) or value != None:
            raise TypeError("next_node must be a Node object")
        return self.__next_node

class SinglyLinkedList:
    """ singly linked list"""
    def __init__(self):
        self.__head