#!/usr/bin/env python3
""" FIFO caching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary with a maximum limit
        - Discards the first item added when the cache is full
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()
        self.order = []  # Tracks insertion order for FIFO

    def put(self, key, item):
        """ Add an item to the cache using FIFO strategy
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is None or item is None:
            return

        # Add or update the item in cache
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item added (FIFO)
                first_key = self.order.pop(0)
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
            self.order.append(key)
        
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        return self.cache_data.get(key)
