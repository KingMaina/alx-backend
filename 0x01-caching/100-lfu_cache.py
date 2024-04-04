#!/usr/bin/env python3

"""LFU Least Frequently Used Cache class

    Adds and retrieves data from the cache using
    the Least Frequently Used (LFU) algorithm
"""
from datetime import datetime
from typing import Dict, List

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A cache system using LFU

        Manages the cache limit using the LFU algorithm and uses
        LRU to handle it when more than one items are selected
        for removal

        Attributes
        ----------
    """
    __lru_counter: Dict[str, List]
    __key_to_remove: str

    def __init__(self):
        """Initializes the cache instance"""
        super().__init__()
        self.__lru_counter = {}

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
            # Find and remove the least frequently used data when cache is full
            if cache_data_len == BaseCaching.MAX_ITEMS:
                freq_counters = {key: value[0] for key,
                                 value in self.__lru_counter.items()}
                freq_sorted = sorted(freq_counters.items(),
                                     key=lambda freq: freq[1])
                # Track cahce data with the same access times
                dups: List = []
                least_frequent = freq_sorted[0]
                for value in freq_sorted:
                    if value[1] == least_frequent[1]:
                        dups.append(value[0])
                # If duplicates exist, use LRU as a tiebreaker
                if (len(dups) > 0):
                    print(len(dups))
                    time_now = datetime.now()
                    deltas = {key: time_now - value[1] for key,
                              value in self.__lru_counter.items()
                              if key in dups}
                    self.__key_to_remove = sorted(deltas.items(),
                                                  key=lambda item: item[1],
                                                  reverse=True)[0][0]
                else:
                    self.__key_to_remove = freq_sorted[0][0]
                data.pop(self.__key_to_remove)
                self.__lru_counter.pop(self.__key_to_remove)
                print("DISCARD: {}".format(self.__key_to_remove))
            self.__lru_counter[key] = [0, datetime.now()]
        self.__lru_counter[key][0] += 1
        self.__lru_counter[key][1] = datetime.now()
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
            self.__lru_counter[key][0] += 1
            self.__lru_counter[key][1] = datetime.now()
        return data
