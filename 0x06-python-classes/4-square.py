#!/usr/bin/python3
"""tache 2 description d'une class vide"""
class Square:
    """ definition de la fonction init de square"""
    def __init__(self, size=0):
        """init function"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for size"""
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        return self.__size



my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)