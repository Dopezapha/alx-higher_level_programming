#!/usr/bin/python3
"""A function that writes a string to a text file and returns count"""


def write_file(filename="", text=""):
    """Definition of function"""
    with open(filename, mode="w", encoding="UTF8") as f:
        count = f.write(text)
    return count
