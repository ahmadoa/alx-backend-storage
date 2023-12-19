#!/usr/bin/env python3
"""9. insert a doc to collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts new doc in a collection based on args"""
    return mongo_collection.insert_one(kwargs).inserted_id
