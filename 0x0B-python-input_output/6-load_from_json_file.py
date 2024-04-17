#!/usr/bin/python3
""" loads from json file module """
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
