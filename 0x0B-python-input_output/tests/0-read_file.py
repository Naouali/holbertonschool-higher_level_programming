#!/usr/bin/python3
"""
module to read a file
"""

def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read())
