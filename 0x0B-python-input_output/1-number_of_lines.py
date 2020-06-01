#!/usr/bin/python3
"""
2
"""


def number_of_lines(filename=""):
    """
    module to count
    lines
    """
    with open(filename) as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
