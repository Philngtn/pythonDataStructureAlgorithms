# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Implementing Class
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #


class MyArray:
    
    def __init__(self):
        self.length = 0
        # Declare as dictionary
        self.data = {}

    # Convert the class object into string
    def __str__(self):
        # convert all the class object to dictionary type {length, data}
        return str(self.__dict__)


    def get(self,index):
        return self.data[index]

    def push(self, item):
        self.data[self.length]= item
        self.length +=1 

    def pop(self):
        lastitem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastitem

    def delete(self, index):
        deleteditem = self.data[index]
        # Shifting the data to one slot
        for i in range(index, self.length -1):
            self.data[i] = self.data[i+1]
        # Delete the last array slot
        del self.data[self.length - 1]
        self.length -= 1
        return deleteditem
      

newArray = MyArray()
newArray.push("Hello. ")
newArray.push("How")
newArray.push("are")
newArray.push("you")
newArray.push("!")

newArray.delete(1)
print(newArray) 
