#!/usr/bin/python3
"""
Module with function print my name
See docstrings
"""
def say_my_name(first_name, last_name=""):
    """ print my name is <first> + <last>"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("my name is {} {}".format(first_name, last_name))
