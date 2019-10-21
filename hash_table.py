# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# KRISTEN ORUE


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
         
        for keyval in self.data[self.hash(key)]:
            if keyval[0] == key:
                keyval[1] = value
                return
        self.data[index].append(keyvalue)

    def __getitem__(self, key):
        
        for keyval in self.data[self.hash(key)]:
            if keyval[0] == key:
                return keyval[1]

    
    def hash(self, key):
        key = hash(key)
        key = key % self.size
        return key  

    def delete(self, key):
        index = self.hash(key)

        for keyval in self.data[self.hash(key)]:
            if keyval[0] == key:
                keyval.remove(key)

    def clear(self):
        self.data = [[],[],[]]
       




