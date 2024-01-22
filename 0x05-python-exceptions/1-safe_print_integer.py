#!/usr/bin/python3

def safe_print_integer(value):
    try:
        input_value = "{:d}".format(value)
        print(input_value)
        return True
    except ValueError:
        return False
