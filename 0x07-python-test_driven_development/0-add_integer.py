#!/usr/bin/python3
"""This is "0-add_integer" module.
This function takes to integer or floats and add
them together. exemple:
>>> add_integer(1, 4)
5
"""


def add_integer(a, b=98):
    """function to add integer"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
