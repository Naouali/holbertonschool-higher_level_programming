#!/usr/bin/python3
"""
module to write to a file
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return(f.write(text))
