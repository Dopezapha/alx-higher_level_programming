#!/usr/bin/python3
"""Module for converting a JSON string to an object."""


def from_json_string(my_str):
    """Definition of a function that converts a JSON str to an obj"""
    import json
    return json.loads(my_str)
