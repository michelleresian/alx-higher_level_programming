#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (number): The divisor for the matrix division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to zero.

    Returns:
        list of lists: The new matrix with elements divided by the divisor,
        rounded to 2 decimal places.
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(error_msg)

    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2)
                   for element in row] for row in matrix]
    return new_matrix
