#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        
        if value < 0:
            raise ValueError("size must be >= 0")
            
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value
        
            
    def area(self):
        size = self.__size
        area = size * size
        return area 
