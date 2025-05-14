#!/usr/bin/env python3
""" LIFO caching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary with a maximum limit
        - Discards the last item added when the cache is full
    """

    def __init__(self):
        """ Initialize the LIFO cache
        """
        super().__init__()
        self.stack = []  # Tracks insertion order for LIFO

    def put(self, key, item):
        """ Add an item to the cache using LIFO strategy
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is None or item is None:
            return

        # If key already exists, update it and move to top of stack
        if key in self.cache_data:
            self.stack.remove(key)
        else:
            # If cache will exceed MAX_ITEMS, remove the last item (LIFO)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop()
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

        # Add or update the item in cache
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        return self.cache_data.get(key)
