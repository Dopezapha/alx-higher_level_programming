#!/usr/bin/python3
"""This is a square class"""

class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """Initialization of instance size"""
        self.size = size  # Calling the size setter

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

