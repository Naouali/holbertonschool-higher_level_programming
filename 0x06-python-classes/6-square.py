#!/usr/bin/python3
class Square:
    """ creatin a square class """
    def __init__(self, size=0, position=(0, 0)):
        """ square parameters"""
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (type(position) == tuple
                and type(position[0]) == int
                and type(position[1]) == int
                and position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        """ setting up position retriver"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setting up  position setter"""
        if type(value) == tuple and type(value[0]) == int and\
           type(value[1]) == int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        def area(self):
            """area retriver"""
            return self.__size * self.__size

    def my_print(self):
        """ print function to print a square"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """size retriver"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
