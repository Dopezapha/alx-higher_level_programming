#!/usr/bin/python3
"""
Module for defining a Student class with filter for to_json method.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        with first, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance with filter
        """
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }
