#!/usr/bin/python3
"""
pascale triangle
"""


def binomial(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)

    return [res]

def pascal_triangle(n):
    """
    pascal triangle
    """
    
    if n <= 0:
        return []
    for j in range(n):
        my_list = []
        for i in range(n + 1):
            my_list.append(binomial(j, i))
    return my_list
