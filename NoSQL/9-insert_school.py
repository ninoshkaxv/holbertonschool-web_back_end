#!/usr/bin/env python3
"""Module inserting a document"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a document in a collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
