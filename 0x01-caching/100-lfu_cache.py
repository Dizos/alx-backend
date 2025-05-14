#!/usr/bin/env python3
""" LFU caching module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary with a maximum limit
        - Discards the least frequently used item when the cache is full
        - Uses LRU algorithm to break ties in frequency
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.freq = {}  # Tracks frequency of each key
        self.lru_order = []  # Tracks recency order for LRU tiebreaker

    def put(self, key, item):
        """ Add an item to the cache using LFU strategy
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is None or item is None:
            return

        # If key exists, update it
        if key in self.cache_data:
            self.lru_order.remove(key)
        else:
            # If cache will exceed MAX_ITEMS, remove least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find minimum frequency
                min_freq = min(self.freq.values())
                # Get keys with minimum frequency
                lfu_keys = [k for k in self.lru_order if self.freq[k] == min_freq]
                # Remove the least recently used among them (first in lru_order)
                lfu_key = lfu_keys[0]
                self.lru_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]

        # Add or update the item in cache
        self.cache_data[key] = item
        self.lru_order.append(key)
        # Update frequency (increment for existing key, initialize for new)
        self.freq[key] = self.freq.get(key, 0) + 1

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        # Update frequency and LRU order
        self.freq[key] += 1
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
