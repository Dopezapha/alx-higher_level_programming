#!/usr/bin/python3
""" A Square class """


class Square:
    """ Define the size of the Square """

    def __init__(self, size=0):
        """ Condition of size of Square """
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError)
