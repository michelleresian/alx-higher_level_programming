#!/usr/bin/python3
"""a module to be imported"""


def add_numbers(a, b=98):
    """
    a function to add two numbers together and return the result
    """
    if type(a) is not (int or float):
        raise TypeError("a must be an integer")
    if type(b) is not (int or float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
