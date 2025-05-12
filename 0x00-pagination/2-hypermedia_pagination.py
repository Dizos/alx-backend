#!/usr/bin/env python3
"""
Module for hypermedia pagination of a baby names dataset.

This module provides a Server class to paginate data from
Popular_Baby_Names.csv, with helper functions for index ranges
and hypermedia metadata.
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
                         for the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of rows, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The page number (1-indexed, default 1).
            page_size (int): The number of items per page (default 10).

        Returns:
            List[List]: The list of rows for the specified page, or an empty
                        list if the page is out of range.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        assert isinstance(page, int), "page must be an integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page > 0, "page must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Retrieve a page of the dataset with hypermedia metadata.

        Args:
            page (int): The page number (1-indexed, default 1).
            page_size (int): The number of items per page (default 10).

        Returns:
            Dict[str, any]: A dictionary containing page_size, page, data,
                            next_page, prev_page, and total_pages.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        data = self.get_page(page, page_size)
        dataset_size = len(self.dataset())
        total_pages = math.ceil(dataset_size / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page * page_size) < dataset_size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
