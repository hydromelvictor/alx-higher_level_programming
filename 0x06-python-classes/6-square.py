#!/usr/bin/python3
"""tache 2 description d'une class vide"""
class Square:
    """ definition de la fonction init de square"""
    def __init__(self, size=0, position=(0, 0)):
        """init function"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not(isinstance(position, tuple)) or len(position) != 2 :
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position
    
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

    def my_print(self):
        """printf function"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                for k in range(self.__position):
                    print(" ", end="")
                print("#", end="")
            print()

    @property
    def position(self):
        """getters functiion for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter functions for position"""
        if not(isinstance(value, tuple)) or len(value) != 2 :
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        return self.__position


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")