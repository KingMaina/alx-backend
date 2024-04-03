#!/usr/bin/env python3

"""Basic Cache class

    Does basic caching tasks like adding
    and retrieving data
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A cache system

        Has no limits
    """

    def put(self, key: str, item):
        """Adds data in the cache using a key

        Parameters
        ----------
        key: str
            The key that identifies the entry for the data
        item: Any
            The data stored in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves data from the cache using a key

            Parameters
            ----------
            key: str
                The key that identifies the data
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
