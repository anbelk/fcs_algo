class HashTable:
    def __init__(self, capacity=4, max_load_factor=0.7):
        self.count = 0
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.max_load_factor = max_load_factor
        self.load_factor = 0

    def _hash(self, key) -> int:
        return hash(key) % self.capacity
    
    def set(self, key, value):
        index = self._hash(key)
        while True:
            if self.buckets[index] is None:
                self.buckets[index] = [key, value]
                self.count += 1
                self._rehash()
                break
            elif self.buckets[index][0] == key:
                self.buckets[index][1] = value
                break
            else:
                index = (index + 1) % self.capacity

    def _get_bucket_index(self, key):
        index = self._hash(key)
        while True:
            if self.buckets[index] is None:
                raise KeyError(key)
            elif self.buckets[index][0] == key:
                return index
            else:
                index = (index + 1) % self.capacity
    
    def get(self, key):
        return self.buckets[self._get_bucket_index(key)][1]

    def delete(self, key):
        index = self._get_bucket_index(key)
        self.buckets[index] = ["<deleted>", None]
        self.count -= 1
    
    def _rehash(self):
        self.load_factor = self.count / self.capacity
        if self.load_factor > self.max_load_factor:
            old_buckets = self.buckets
            self.capacity *= 2
            self.buckets = [None] * self.capacity
            self.count = 0
            for bucket in old_buckets:
                if bucket is not None:
                    self.set(*bucket)