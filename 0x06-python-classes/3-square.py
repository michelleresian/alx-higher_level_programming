#!/usr/bin/python3
"""A module to export a square with size private attribute"""


class Square:
    """A blue print for a square"""

    def __init__(self, size=0):
        """
        initializing a new instance.

        Args:
        size (int): The size of the new square.
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        A method that returns the area of the square
        """
        return (self.__size * self.__size)
