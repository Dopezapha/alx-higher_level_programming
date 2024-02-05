#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return [attribute for attribute in dir(obj)]
