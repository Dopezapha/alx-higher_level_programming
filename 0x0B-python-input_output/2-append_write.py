#!/usr/bin/python3
"""A function that appends a string and returns count"""


def append_write(filename="", text=""):
    """Append a string at the end of the file"""
    with open(filename, mode="a", encoding="UTF8") as f:
        count = f.write(text)
    return count
