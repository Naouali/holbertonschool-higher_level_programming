#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function to divide a matrix)"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be an integer")
    msg2 = " Each row of the matrix must have the same size"
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError(msg2)
    new = []
    for i in matrix:
        mini = []
        for j in i:
            if type (j) != int and type(j) != float:
                raise TypeError(msg)
            z = round(j/div, 2)
            mini.append(z)
        new.append(mini)
    return new
            
