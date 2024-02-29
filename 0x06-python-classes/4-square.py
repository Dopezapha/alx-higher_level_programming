#!/usr/bin/python3
"""A class Square that defines a square by based on 3-square.py"""


class Square:
    """This is a Square class"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.__size = size

    @property
    def size(self):
        """Getter method for retrieving the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the value of the size attribute."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2
