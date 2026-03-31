#!/usr/bin/env python3
""" 9-insert_school.py: inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection using kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs representing the document fields

    Returns:
        The _id of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
