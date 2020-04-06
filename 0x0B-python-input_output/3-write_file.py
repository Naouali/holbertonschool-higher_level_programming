#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        new = f.write(text)
        return new
