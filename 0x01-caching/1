#!/usr/bin/env python3
""" Basic caching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system that:
        - Inherits from BaseCaching
        - Stores items in a dictionary without any size limit
        - Allows adding and retrieving items by key
    """

    def put(self, key, item):
        """ Add an item to the cache
            Args:
                key: The key for the item
                item: The item to be stored
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key
            Args:
                key: The key of the item to retrieve
            Returns:
                The item associated with the key, or None if key doesn't exist
        """
        return self.cache_data.get(key)
