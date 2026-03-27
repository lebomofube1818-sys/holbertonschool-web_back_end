#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any
from simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Reads the CSV file only once and caches it.
        Returns the dataset as a list of lists, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of the dataset.

        Args:
            page (int): page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            list of lists: a subset of the dataset corresponding to the page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing hypermedia pagination info.

        Args:
            page (int): current page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            dict: containing page_size, page, data, next_page,
                  prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
