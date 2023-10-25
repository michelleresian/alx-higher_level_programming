#!/usr/bin/python3
"""Square class"""


class Square:
    """Define square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set current position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of a square"""

        return self.__size**2

    def my_print(self):
        """
        Print the square with the '#' character.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print("")
