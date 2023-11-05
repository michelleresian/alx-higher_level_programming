#!/usr/bin/python3
"""A module to export a square with size private attribute"""


class Square:
    """A blue print for a square"""

    def __init__(self, number):
        self.__size = number
