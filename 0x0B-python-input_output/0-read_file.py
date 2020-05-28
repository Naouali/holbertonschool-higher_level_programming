#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        for i in f:
            print(i, end="")
