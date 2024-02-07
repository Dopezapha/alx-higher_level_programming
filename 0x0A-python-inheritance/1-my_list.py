#!/usr/bin/python3
"""A class MyList that inherits from list"""


class Mylist(list):
    """Child class Mylist"""

    def print_sorted(self):
        """Definition of sorted printed list"""
        sorted_list = sorted(self)
        print(sorted_list)
