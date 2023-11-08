#!/usr/bin/python3
"""import rectangle subclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """square class"""

    def __init__(self, size):
        """intialization of square sizes"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """print string representation of a square"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """returns the areas of squares"""
        return self.__size ** 2
