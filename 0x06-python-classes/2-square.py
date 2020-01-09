#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if int(size) < 0:
            print("size must be >= 0", end="")
            raise ValueError
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        else:
            self.__size = size
