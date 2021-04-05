from typing import Sized


class HashTable:
    def __init__(self, size):
        self.data = [[] for i in range(size)]
        self.array_length = size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            # ord() returns the order number of the letter in the ASCII table 
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

    def keys(self):
        keysArray = []
        for i in self.data:
            if (bool(i)):
                # Prevent collision
                if (len(i) > 1):
                    for j in i:
                        keysArray.append(j[0])
                else: 
                    keysArray.append(i[0][0])
        return keysArray


hashObj = HashTable(2)
hashObj.set('Chickenpie',19)
hashObj.set('Organge',29)
hashObj.set('Apple',49)
hashObj.set('Grapes',19)


# a = hashObj.get('Grapes')
b = hashObj.keys()

# print(a)
print(b)