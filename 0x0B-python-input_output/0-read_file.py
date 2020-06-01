#!/usr/bin/python3
"""
module to read files
"""


def read_file(filename=""):
    with open(filename) as f:
        for i in f:
            print(i, end="")
