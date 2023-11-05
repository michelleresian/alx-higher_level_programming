#!/usr/bin/python3
"""A module to export a square with size private attribute"""


class Square:
    """A blue print for a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initializing a new instance.

        Args:
        size (int): The size of the new square.
        position (int, int): A tuple contains the position of # to be printed.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        A method that returns the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """A property to retrieve the size private attribute"""
        return self.__size

    @property
    def position(self):
        """A property to retrieve the position of the instance"""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            type(value) != tuple or
            len(value) != 2 or
            (
                type(value[0]) != int or
                type(value[1]) != int
            )
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
