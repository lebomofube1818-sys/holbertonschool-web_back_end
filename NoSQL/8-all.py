#!/usr/bin/env python3
"""8-all.py: Lists all documents in a PyMongo collection"""


def list_all(mongo_collection):
    """Return all documents in a PyMongo collection as a list"""
    return list(mongo_collection.find())
