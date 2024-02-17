#!/usr/bin/python3
"""Module for converting an object to a JSON str."""


def to_json_string(my_obj):
    """Definition of a JSON representation of an object (str)."""
    import json
    return json.dumps(my_obj)
