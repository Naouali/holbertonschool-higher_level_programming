#!/usr/bin/python3
"""
module to append string
at the end of a file
"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return(f.write(text))
