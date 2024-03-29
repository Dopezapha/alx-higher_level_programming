#!/usr/bin/python3
"""
This module contains a class MagicClass that performs the
same functionality as the provided Python bytecode.
"""

import math


class MagicClass:
    """
    This class represents a MagicClass with the
    same functionality as the provided bytecode.
    """

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes and returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes and returns the circumference of the circle."""
        return 2 * math.pi * self.__radius
