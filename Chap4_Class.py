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

     


newArray = MyArray()
newArray.push("Hello. ")
newArray.push("How")
newArray.push("are")
newArray.push("you")
newArray.push("!")
print(newArray.pop())
print(newArray) 
