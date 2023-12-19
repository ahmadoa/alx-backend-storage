#!/usr/bin/env python3
"""8- lists all docs using py"""


def list_all(mongo_collection):
    """lists all docs in a collection"""
    return list(mongo_collection.find())
