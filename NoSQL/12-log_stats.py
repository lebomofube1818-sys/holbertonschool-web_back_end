#!/usr/bin/env python3
""" 12-log_stats.py: provides stats about Nginx logs """

from pymongo import MongoClient


if __name__ == "__main__":
    """Main function to display log stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    # Methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status count
    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")
