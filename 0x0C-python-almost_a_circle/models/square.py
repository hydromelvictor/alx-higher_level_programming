#!/usr/bin/python3
"""
squared class
"""


import rectangle
Rectangle = rectangle.Rectangle

class Square(Rectangle):
    """inheritance of rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        size: square dimension
        x: position in i
        y: position in j
        id: identifier
        """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """string format
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
            self.y, self.width)

    @property
    def size(self):
        """size getters
        """
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updating
            args: variadic arguments
        """
        arg = [self.id, self.width, self.x, self.y]

        if len(args) != 0:
            for i in range(len(args)):
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]

                if i == 2:
                    self.x = args[i]

                if i == 3:
                    self.y = args[i]

                if i == 0:
                    self.id = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]

                if key == "x":
                    self.x = kwargs[key]

                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """dictionary
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
