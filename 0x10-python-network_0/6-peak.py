#!/usr/bin/python3
def find_peak(list_of_integers):
    """function ro find a peak in
    one D array
    """
    value = None
    a = list_of_integers[1:]
    for i in range(len(a)-1):
        if a[i] >= a[i+1] and a[i] >= a[i-1]:
            value = a[i]
    return value

