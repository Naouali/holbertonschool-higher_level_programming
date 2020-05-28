#!/usr/bin/python3
"""
module to calculate
number of lines in a file
"""

def number_of_lines(filename=""):
    with open(filename) as f:
        count = 0
        for i in f:
            count += 1
    return count

