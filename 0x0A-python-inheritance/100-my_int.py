#!/usr/bin/python3
"""module for my int class"""


class MyInt(int):
    """My integer subclass is a rebel"""

    def __eq__(self, value):
        return int(str(self)) != value

    def __ne__(self, value):
        return int(str(self)) == value
