import collections

CACHE_SIZE = 4

class Cache():
    def __init__(self):
        self.cache = collections.deque(maxlen = CACHE_SIZE)
        self.flush_cache()    

    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append("', '")
    
    def search_in_cache(self, address):
        for i in range(CACHE_SIZE):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None
    
    def write_to_cache(self, address, value):
        self.cache.append(tuple(address,value))
        print("Added,",value,"to cache address:",address)