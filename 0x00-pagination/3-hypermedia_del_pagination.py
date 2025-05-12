#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: A dictionary mapping indices to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of the dataset starting at the specified index.

        Args:
            index (int, optional): The starting index (0-based, default None).
                                   If None, starts at 0.
            page_size (int): The number of items per page (default 10).

        Returns:
            Dict: A dictionary containing:
                - index: Current start index.
                - next_index: Index of the first item after the current page.
                - page_size: Number of items in the current page.
                - data: List of rows for the current page.

        Raises:
            AssertionError: If index is negative or out of range.
        """
        assert isinstance(index, (int, type(None))), "index must be an integer or None"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page_size > 0, "page_size must be greater than 0"

        # Default to index 0 if None
        index = 0 if index is None else index
        assert index >= 0, "index must be non-negative"

        indexed_data = self.indexed_dataset()
        max_index = len(indexed_data)
        assert index < max_index, "index out of range"

        data = []
        current_index = index
        items_collected = 0
        next_index = None

        # Collect up to page_size items, skipping missing indices
        while items_collected < page_size and current_index < max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        # Set next_index to the next valid index after the current page
        next_index = current_index if current_index < max_index else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
