#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function to divide a matrix)"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be an integer")
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    for i in matrix:
        mini = []
        for j in i:
            if type (j) != int and type(j) != float:
                raise TypeError(msg)
                break
            z = round(j/div, 2)
            mini.append(z)
        new.append(mini)
    return new
            
