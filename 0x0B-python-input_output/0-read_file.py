#!/usr/bin/python3
"""A function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Reads the content of a file and prints it."""
    with open(filename, mode = "r", encoding="utf-8") as f:
        print(f.read(), end="")
