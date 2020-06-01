#!/usr/bin/python3
"""
2
"""


def read_lines(filename="", nb_lines=0):
    """
    read lines
    """
    with open(filename) as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
