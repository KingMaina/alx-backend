#!/usr/bin/env python3#!/usr/bin/env python3

"""MRU Most Recently Used Cache class

    Adds and retrieves data from the cache using
    the Most Recently Used (MRU) algorithm
"""
from datetime import datetime
from typing import Union, Dict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A cache system using MRU

        Manages the cache limit using the MRU algorithm

        Attributes
        ----------
        __mfu_counter: Dict[str, List]
            Dictionary that tracks the most frequently accessed resource
            and the time it was added/modified
        __key_to_remove: str
            Key that maps to the data in the cache
    """
    __mru_tracker: Dict[str, datetime]
    __key_to_remove: Union[str, None]

    def __init__(self):
        """Initializes the cache instance"""
        super().__init__()
        self.__key_to_remove = None
        self.__mru_tracker = {}

    def put(self, key: str, item):
        """Adds data in the cache using a key

        Parameters
        ----------
        key: str
            The key that identifies the entry for the data
        item: Any
            The data stored in the cache
        """
        if key is None or item is None:
            return
        data = self.cache_data.copy()
        cache_data_keys: list = list(data.keys())
        cache_data_len: int = len(cache_data_keys)

        # Add the data if the key does not exist
        if key not in cache_data_keys:
            # Find and remove the most recently used data when cache is full
            if cache_data_len == BaseCaching.MAX_ITEMS:
                time_now = datetime.now()

                # Calculate time since data was last added/modified
                deltas = {key: time_now - value for key,
                          value in self.__mru_tracker.items()}

                # Sort the time deltas in descending order and
                # select the data with the smallest delta to be removed
                self.__key_to_remove = sorted(deltas.items(),
                                              key=lambda item: item[1])[0][0]

                # Remove the most recently used data
                data.pop(self.__key_to_remove)
                self.__mru_tracker.pop(self.__key_to_remove)
                print("DISCARD: {}".format(self.__key_to_remove))
                self.__key_to_remove = None  # Reset key to be removed
        self.__mru_tracker[key] = datetime.now()
        data.update({key: item})
        self.cache_data = data

    def get(self, key):
        """Retrieves data from the cache using a key

            Parameters
            ----------
            key: str
                The key that identifies the data
        """
        if key is None:
            return None
        data = self.cache_data.get(key, None)
        if data is not None:
            self.__mru_tracker[key] = datetime.now()
        return data
