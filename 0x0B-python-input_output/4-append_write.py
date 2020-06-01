#!/usr/bin/python3
"""
4
"""


def append_write(filename="", text=""):
    """
    function
    to append line
    """
    with open(filename, 'a') as f:
        new = f.write(text)
        return new
