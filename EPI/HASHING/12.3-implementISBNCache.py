from collections import OrderedDict

class LruCache:
    def __init__(self, capacity):
        # Map of (isbn, price) pair
        self.cache = OrderedDict()
        self.capacity = capacity 

    def getIsbn(self, isbn):
        # Obtain the price and make it MRU
        if isbn not in self.cache:
            return -1 
        price = self.cache.pop(isbn)
        # Since map inserts value based on order of insertion, it is re-inserted and becomes MRU
        self.cache[isbn] = price 
        return price 
    
    def insertIsbn(self, isbn, price):
        # If already exists, get price and make it MRU
        if isbn in self.cache:
            price = self.cache.pop(isbn)
        elif len(self.cache) == self.capacity:
            # If cache hits capacity, we remove LRU
            # last=False, evicts LRU; last=True, evicts MRU
            self.cache.popitem(last=False)
        self.cache[isbn] = price

    def eraseIsbn(self, isbn):
        return self.cache.pop(isbn, None) is not None
