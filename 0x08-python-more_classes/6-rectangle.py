#!/usr/bin/python3
"""
area and rectange module
"""


class Rectangle:
    """ Rectangle class
    width : rectangle width
    height: rectange height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        method called
        every time insatnce
        deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(self.__height):
            s += ("#" * self.__width + "\n")
        return s[:-1]

    def __repr__(self):
        """return a string represenation
        of the rectange instance
        """
        return 'Rectangle({}, {})'.format(self.__width, self.height)

    @property
    def width(self):
        """retrive the rectange widht:
        Return:
        int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set rectange width
        Args:
        int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive rectanle height
        Return:
        int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set rectangle height
        Args:
        int
        """
        if type(value) != int:
            raise TypeError("height must be and integer")
        if value < 0:
            raise ValueError("height musy be >= 0")
        self.__height = value
