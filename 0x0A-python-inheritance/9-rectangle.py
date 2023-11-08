#!/usr/bin/python3
"""class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class inheriting form the base geometry class."""

    def __init__(self, width, height):
        """class instatiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function to calculate area"""
        return self.__height * self.__width

    def __str__(self):
        """string representation of rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
