# Last updated: 3/15/2026, 8:19:28 PM
1from collections import OrderedDict
2
3class LRUCache:
4    def __init__(self, capacity):
5        self.capacity = capacity
6        self.cache = OrderedDict() # This tracks BOTH data and order
7
8    def get(self, key):
9        if key not in self.cache:
10            return -1
11        # "Touch" the item: move it to the end (Most Recently Used)
12        self.cache.move_to_end(key)
13        return self.cache[key]
14
15    def put(self, key, value):
16        if key in self.cache:
17            # Update and move to the end
18            self.cache.move_to_end(key)
19        self.cache[key] = value
20        
21        # If we have too many items, delete the oldest one (the first one)
22        if len(self.cache) > self.capacity:
23            self.cache.popitem(last=False)