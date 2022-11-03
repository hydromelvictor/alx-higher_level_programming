#!/usr/bin/python3
"""rectangle class
"""

import json
import os


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """id: id for init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file json
        """
        filename = cls.__name__ + ".json"
        obj = cls.to_json_string(list_objs)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(obj)

    @staticmethod
    def from_json_string(json_string):
        """deserialization of json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating functions"""
        return cls(4, 2, 1).update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """loads form file"""
        filename = cls.__name__ + ".json"

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                for i in file:
                    cls.from_json_string(i)
        else:
            return []


class Rectangle(Base):
    """class inheritance of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ width: rectangle width
            height: rectangle height
            x: coord for i
            y: coord for j
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @property
    def height(self):
        """getter for height
        """
        return self.__height

    @property
    def x(self):
        """getter for x
        """
        return self.__x

    @property
    def y(self):
        """getter for y
        """
        return self.__y

    @width.setter
    def width(self, width):
        """setter for width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """setter for height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """setter for x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter for y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area is product of width and height
        """
        return self.__height * self.__width

    def display(self):
        """rectangle displayer
        """
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")

            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string format methode
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ updating
            args: variadic arguments
        """
        arg = [self.id, self.__width, self.__height, self.__x, self.__y]

        if len(args) != 0:
            for i in range(len(args)):
                if i == 1:
                    if type(args[i]) is not int:
                        raise TypeError("width must be an integer")

                    if args[i] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = args[i]

                if i == 2:
                    if type(args[i]) is not int:
                        raise TypeError("height must be an integer")

                    if args[i] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = args[i]

                if i == 3:
                    if type(args[i]) is not int:
                        raise TypeError("x must be an integer")

                    if args[i] < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = args[i]

                if i == 4:
                    if type(args[i]) is not int:
                        raise TypeError("y must be an integer")

                    if args[i] < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = args[i]

                if i == 0:
                    self.id = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]

                if key == "width":
                    if type(kwargs[key]) is not int:
                        raise TypeError("width must be an integer")

                    if kwargs[key] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = kwargs[key]

                if key == "height":
                    if type(kwargs[key]) is not int:
                        raise TypeError("height must be an integer")

                    if kwargs[key] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = kwargs[key]

                if key == "x":
                    if type(kwargs[key]) is not int:
                        raise TypeError("x must be an integer")

                    if kwargs[key] < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = kwargs[key]

                if key == "y":
                    if type(kwargs[key]) is not int:
                        raise TypeError("y must be an integer")

                    if kwargs[key] < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """dictionary
        """
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
