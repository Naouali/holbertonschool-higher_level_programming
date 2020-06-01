#!/usr/bin/python3
"""
module to read files
"""


def read_file(filename=""):
    """
    function to
    read file
    """
    with open(filename) as f:
        for i in f:
            print(i, end="")
