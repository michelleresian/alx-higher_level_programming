#!/usr/bin/python3

""" Rectangle class. """


class Rectangle:
    """Defining a rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize the width and the heigth of the rectangle. """

        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Area of a Rectangle"""

        return self._width * self._height

    def perimeter(self):
        """Perimeter"""

        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """ String representation of the rectangle."""

        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = self.print_symbol * self._width + "\n"
        rectangle_str *= self._height
        return rectangle_str

    def __repr__(self):
        """ String representation of the rectangle"""

        return "{:s}({:d}, {:d})".format((type(self).__name__),
                                         self._width, self._height)

    def __del__(self):
        """kill Rectangle dec inst count"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return larger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """initialize a square instance"""
        return cls(size, size)
