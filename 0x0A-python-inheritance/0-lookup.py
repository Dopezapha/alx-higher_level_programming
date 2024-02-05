#!/usr/bin/python3

def lookup(obj):
    """Definition of an object lookup.

    Returns:
        list: A list of attributes and methods of the input object.
    """
    return dir(obj)
