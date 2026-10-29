# Hash Table from FreeCodeCamp.org
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)
        bucket = self.collection.get(hashed)
        if bucket is not None and key in bucket:
            del bucket[key]
            if not bucket:
                del self.collection[hashed]

    def lookup(self, key):
        hashed = self.hash(key)
        bucket = self.collection.get(hashed)
        if bucket is not None:
            return bucket.get(key)
        return None