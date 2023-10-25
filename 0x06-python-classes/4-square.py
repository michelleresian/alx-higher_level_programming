#!/usr/bin/python3
"""Square class"""


class Square:
    """Define square class"""

    def __init__(self, size=0):
        """Initialize class"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """int: private size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Area of a square"""

        return self.__size**2
