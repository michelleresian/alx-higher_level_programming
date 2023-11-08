#!/usr/bin/python3
"""
BaseGeometry class.
"""


class BaseGeometry:
    """
    Defines area.
    """

    def area(self):
        """
        Compute the area of the geometry shape.

        Raises:
            Exception: Indicating that the area()
            method is not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
