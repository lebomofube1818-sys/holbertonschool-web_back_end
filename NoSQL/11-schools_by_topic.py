#!/usr/bin/env python3
""" 11-schools_by_topic.py: returns schools by topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        A list of matching school documents
    """
    return list(mongo_collection.find({"topics": topic}))
