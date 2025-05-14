#!/usr/bin/env python3
""" LRU caching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a Least Recently Used caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary with a maximum limit
        - Discards the least recently used item when the cache is full
    """

    def __init__(self):
        """ Initialize the LRU cache
        """
        super().__init__()
        self.lru_order = []  # Tracks usage order for LRU

    def put(self, key, item):
        """ Add an item to the cache using LRU strategy
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is None or item is None:
            return

        # If key exists, update it and move to end (most recent)
        if key in self.cache_data:
            self.lru_order.remove(key)
        else:
            # If cache will exceed MAX_ITEMS, remove least recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]

        # Add or update the item in cache
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        # Update LRU order: move accessed key to end (most recent)
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
