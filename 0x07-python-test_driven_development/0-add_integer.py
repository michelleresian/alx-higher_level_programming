#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers and returns their sum.

    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added (default is 98).

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Returns:
        int: The sum of the two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
