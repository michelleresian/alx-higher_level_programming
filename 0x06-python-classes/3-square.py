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

    def area(self):
        """Area of a square"""

        return self.__size**2
