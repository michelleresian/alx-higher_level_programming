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
        self.__size = size

    def area(self):
        """
        A method that returns the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """A property to retrieve the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """A method to print the size of a square"""
        if (self.__size == 0):
            print("\n", end="")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
