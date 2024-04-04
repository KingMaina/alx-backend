# Caching💾

## Introduction

This project covers the concept of caching and the different types of caching systems. It also covers the different algorithms used in caching systems.

## Learning Objectives

* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have

## Basic Cache

A cache is a hardware or software component that stores data so that future requests for that data can be served faster. The data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere. A `cache hit` occurs when the requested data is found in a cache, while a `cache miss` occurs when it is not. In this cache system, the cache is implemented using a dictionary and there are no limits to the size of the cache. This is demonstrated in the `0-basic_cache.py` file.

## FIFO(First In, First Out)

FIFO is an acronym for `First In, First Out`. It is used to manage data storage in such a way that the first item stored in the data structure is the first item retrieved. This is analogous to a queue - a line of people waiting for a service. The first person in line is the first person to be served. In this cache system, the first item added to the cache is the first item to be removed when the cache is full. This is demonstrated in the [1-fifo_cache.py](1-fifo_cache.py) file.

## LIFO (Last In, First Out)

LIFO is an acronym for `Last In, First Out`. It is used to manage data storage in such a way that the last item stored in the data structure is the first item retrieved. This is analogous to a stack of plates - the last plate placed on the stack is the first plate to be removed.
In this cache system, the most recently added item is the first item to be removed when the cache is full. This is demonstrated in the [2-lifo_cache.py](2-lifo_cache.py) file.

## LRU (Least Recently Used)

LRU is an acronym for `Least Recently Used`. It is used to manage data storage in such a way that the least recently used item is the first item to be removed. This is analogous to a cache - the least recently used item is the first item to be removed. The idea behind LRU is that if an item has not been used in a long time, it is unlikely to be used again in the near future. This is demonstrated in the [3-lru_cache.py](3-lru_cache.py) file.

## MRU (Most Recently Used)

MRU is an acronym for `Most Recently Used`. It is used to manage data storage in such a way that the most recently used item is the first item to be removed. This is analogous to a cache - the most recently used item is the first item to be removed. The idea behind MRU is that if an item has been used recently, it is likely to be used again in the near future. This is demonstrated in the [4-mru_cache.py](4-mru_cache.py) file.

## LFU (Least Frequently Used)

LFU is an acronym for `Least Frequently Used`. It is used to manage data storage in such a way that the least frequently used item is the first item to be removed. 
* This is analogous to a cache - the least frequently used item is the first item to be removed. The idea behind LFU is that if an item has not been used frequently, it is unlikely to be used again in the near future.
* In this cache system, the least frequently used item is the first item to be removed when the cache is full. If there is a tie (i.e., two or more items have been used the same number of times), the least recently used item is removed.This is demonstrated in the [100-lfu_cache.py](100-lfu_cache.py) file.