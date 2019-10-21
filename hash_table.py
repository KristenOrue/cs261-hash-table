# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = []
        self.keys = []

        for i in range(0,self.size):
            self.data.append([])


    def __setitem__(self, key, value):

         keyvalue = [key,value]
         index = self.hash(key)
         self.data[index].append(keyvalue)

    def __getitem__(self, key):
        for k in self.keys:
            if k == key:
                return self.data[k]
        return None
    
    def hash(self, key):
        key = hash(key)
        key = key % self.size
        return key  


