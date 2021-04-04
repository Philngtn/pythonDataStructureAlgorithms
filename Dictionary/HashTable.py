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
        # If there is no [] data in big [[],[],...,[]]
        # set it empty
        # bool returns [] = false, [1,2] = true
        if (not bool(self.data[address])):
            self.data[address] = []        
        
        self.data[address].append([key,value])
        
        print(self.data)
        return self.data

    def get(self,key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if (currentBucket):
            for i in range(len(currentBucket)):
                if(currentBucket[i][0] == key):
                    return currentBucket[i][1]
        return None


hashObj = HashTable(2)
hashObj.set('grapes',19)
hashObj.set('grapsdes',1249)
a = hashObj.get('grapes')

print(a)