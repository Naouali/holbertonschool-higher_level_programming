#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        string = str[n + 1:]
        new = str[:n] + string
        return new
    else:
        return str
