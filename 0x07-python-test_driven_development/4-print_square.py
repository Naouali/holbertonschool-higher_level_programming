#!/usr/bin/python3
def print_square(size):
    """function to print a square"""
    if size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) != int:
        raise TypeError("size must be an integer")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    
