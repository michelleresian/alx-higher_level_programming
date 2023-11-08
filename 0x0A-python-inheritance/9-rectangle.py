#!/usr/bin/python3
"""A module for a class that calculate the Geometry of an object"""


class BaseGeometry:
    """A class to calculate the Geometry"""

    def area(self):
        """A function to raise error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public method to validate the value"""
        if (type(value) != int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A rectangle that inherits from BaseGeometry class (being a subclass to it and inherits all attributes)
    """

    def __init__(self, width, height):
        """
        initiate inherited attributes and validate it
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A method to return the area of the object"""
        return (self.__width * self.__height)

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
