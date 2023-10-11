#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr = [[number ** 2 for number in row] for row in matrix]

    return sqr
