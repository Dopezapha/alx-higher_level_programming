#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for retrieving the value of the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for setting the value of the position attribute."""
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        result = []
        for _ in range(self.__position[1]):
            result.append('')
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return '\n'.join(result)
