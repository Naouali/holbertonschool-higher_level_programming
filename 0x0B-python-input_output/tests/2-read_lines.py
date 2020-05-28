#!/usr/bin/python3
"""
module to print n 
line from file
"""
number_of_lines = __import__('1-number_of_lines').number_of_lines

def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0: 
            for line in f:
                print(line, end='')
        else: 
            for i in range(nb_lines): 
                print(f.readline(), end='')
