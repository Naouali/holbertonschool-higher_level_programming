#!/usr/bin/python3
"""
rectangle module
"""


class Rectangle:
    """class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """define a rectange by its width and height"""
        self.width = width
        self.height = height

    @property
    """retrive the width attribute"""
    def width(self):
        return self.__widht

    @width.setter
    """set the width sttribute"""
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) != int:
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    """retrive the height"""
    def height(self):
        return self.__height

    @height.setter
    """set the height attribue"""
    def height(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) != int:
            raise TypeError("width must be an integer")
        else:
            self.__height = value
