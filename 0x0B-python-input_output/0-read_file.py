#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads the content of a file and prints it."""
    if filename:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    else:
        print("Please provide a valid filename.")
