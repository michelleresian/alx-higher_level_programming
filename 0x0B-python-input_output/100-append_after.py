#!/usr/bin/python3
"""define an insertion function at a specific point"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text at a specific line function"""
    string = ""
    with open(filename, "r") as file:
        for line in file:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, 'w') as file:
        file.write(string)
