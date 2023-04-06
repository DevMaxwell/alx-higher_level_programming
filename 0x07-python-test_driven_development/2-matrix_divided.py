#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ divide through matrix by div arg """
    result = []
    # check empty matrix
    if not matrix or matrix is [[]] or matrix is None:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    # check for non int/float type, and no arg for 'div'
    if type(div) is not int or type(div) is not float or div is None:
        raise TypeError("div must be a number")
    # check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # determining length of matrix 1
    if matrix[0]:
        leng = len(matrix[0])
    else:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)

    # loop through matrix and divide each element by 'div'
    for i in range(len(matrix)):
        if len(matrix[i]) != leng:
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for j in matrix[i]:
            err = "matrix must be a matrix (list of lists)"
            err += " of integers/f    loats"
            if type(j) is not int or type(j) is not float:
                raise TypeErroe(err)
            else:
                result[i].append(round(j / div, 2))
    return result
