from typing import Sized


class HashTable:
    def __init__(self, size):
        self.data = [[] for i in range(size)]
        self.array_length = size



    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.array_length
            # print(hash)
        return hash

    def set(self,key,value):
        address = self._hash(key)
        if (not bool(self.data[address])):
            self.data[address] = [key,value]
            print(self.data)




hashObj = HashTable(50)

hashObj.set('grapes',19)

