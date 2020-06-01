#!/usr/bin/python3
"""
3
"""


def write_file(filename="", text=""):
    """
    write into
    file
    """
    with open(filename, 'w') as f:
        new = f.write(text)
        return new
