#!/usr/bin/python3
"""This is a class add integer"""


def add_integer(a, b=98):
    """A function for integer addition"""
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile('add_integer_doctest.txt')
