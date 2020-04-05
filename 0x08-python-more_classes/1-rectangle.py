#!/usr/bin/python3
"""
rectangle module
"""


class Rectangle:
    """class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """define a rectange by its width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrive the width attribute
        Returns: 
        int
        """
        return self.__widht

    @width.setter
    def width(self, value):
        """set the width sttribute
        Args:
        int
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """retrive the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height attribute"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__height = value
