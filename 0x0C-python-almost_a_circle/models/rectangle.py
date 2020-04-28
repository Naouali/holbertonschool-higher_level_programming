#!/usr/bin/python3
"""
rectange module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """print rectagle with #"""
        s = ""
        for i in range(self.height):
            s += (" " * self.x + "#" * self.width + "\n")
        print("\n" * self.y + s[:-1])

    def __str__(self):
        """create str representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """list of argument"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for k, v in kwargs.items():
                if k == "y":
                    self.y = kwargs[k]
                if k == "x":
                    self.x = kwargs[k]
                if k == "width":
                    self.width = kwargs[k]
                if k == "height":
                    self.height = kwargs[k]
                if k == "id":
                    self.id = kwargs[k]

    def to_dictionary(self):
        """
        return dict representation
        """
        return {"id": self.id,
                "width": self. width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
