#!/bin/bash
echo '
# FIFO Cache Implementation

This project implements a FIFO (First-In-First-Out) caching system in Python. The cache inherits from the `BaseCaching` class and adheres to the following requirements:

## Requirements
- Python 3.7 on Ubuntu 18.04 LTS
- Files must be executable and start with `#!/usr/bin/env python3`
- Code must follow pycodestyle (version 2.5)
- All modules, classes, and functions must have documentation
- Files must end with a newline
- Maximum cache size is defined by `BaseCaching.MAX_ITEMS` (4 items)

## Files
- `base_caching.py`: Contains the parent `BaseCaching` class
- `fifo_cache.py`: Implements the `FIFOCache` class with FIFO caching logic
- `README.md`: This file

## Usage
The `FIFOCache` class provides:
- `put(key, item)`: Adds an item to the cache. If the cache is full, the oldest item is discarded.
- `get(key)`: Retrieves an item by key, or returns None if the key doesn't exist.
- `print_cache()`: Prints the current cache contents (inherited from `BaseCaching`).

Example:
```python
from fifo_cache import FIFOCache

cache = FIFOCache()
cache.put("A", "Apple")
cache.put("B", "Banana")
cache.print_cache()
# Output:
# Current cache:
# A: Apple
# B: Banana

cache.put("C", "Cherry")
cache.put("D", "Date")
cache.put("E", "Elderberry")  # This causes the oldest item (A) to be discarded
# Output:
# DISCARD: A

print(cache.get("B"))  # Output: Banana'
