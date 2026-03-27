#!/usr/bin/env python3
"""
Hypermedia pagination module
"""

import math
from typing import List, Dict, Any
from simple_helper_function import index_range
import csv


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset without headers.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.

        Args:
            page (int): page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            List[List]: the requested page of data
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with hypermedia pagination info.

        Args:
            page (int): current page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            Dict[str, Any]: containing page_size, page, data, next_page,
                            prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        # Determine next_page
        next_page = page + 1 if page < total_pages else None
        # Determine prev_page
        if page <= 1:
            prev_page = None
        elif page > total_pages:
            prev_page = total_pages
        else:
            prev_page = page - 1

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
