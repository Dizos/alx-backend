#!/usr/bin/env python3
""" MRU caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a Most Recently Used caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary with a maximum limit
        - Discards the most recently used item when the cache is full
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.mru_order = []  # Tracks usage order for MRU

    def put(self, key, item):
        """ Add an item to the cache using MRU strategy
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is None or item is None:
            return

        # If key exists, update it and move to end (most recent)
        if key in self.cache_data:
            self.mru_order.remove(key)
        else:
            # If cache will exceed MAX_ITEMS, remove most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.mru_order.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]

        # Add or update the item in cache
        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        # Update MRU order: move accessed key to end (most recent)
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
