#!/usr/bin/python3
"""
module to print a rectangle
"""


class rectangle:
	"""class to print
	rectagle
	"""
	def __init__(self, width=0, height=0):
        self.widht = width
        self.height = height

    def area(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            s += ("#" * self.__width + "\n")
        return s[:-1]

    def __repr(self):
        

    @proprety
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TYpeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        
		
