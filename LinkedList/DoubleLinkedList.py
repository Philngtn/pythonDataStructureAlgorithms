# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 3: Linked List
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# 10 - 20 - a - 30 - 40 

from typing import NoReturn


class doubleNode:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    
    def __init__(self):
       self.head = None
       self.tail = None
       self.length = 0

    def append(self, value):
        newDoubleNode = doubleNode(value)

        if (self.length == 0):
            self.head = newDoubleNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newDoubleNode
            newDoubleNode.prev = self.tail
            self.tail = newDoubleNode
            self.length += 1
    
    def prepend(self, value):
        newDoubleNode = doubleNode(value)

        if (self.length == 0):
            self.head = newDoubleNode
            self.tail = self.head
            self.length += 1
        else:
            newDoubleNode.next = self.head
            self.head = newDoubleNode
            self.length += 1

    def insert(self, value, location):
        newDoubleNode = doubleNode(value)
        count = 0
        temp = self.head
        if (self.length == 0):
            self.head = newDoubleNode
            self.tail = self.head
            self.length += 1
            return 0
        
        if (location > self.length or location < 0):
            return "Error: location is out of scope !!!"
        
        while(True):
            if location > self.length:
                self.append(value)
                break
            elif location == 0:
                self.prepend(value)
                break
            else:
                if (count != (location -1)):
                    temp = temp.next
                    count +=1
                else:
                    newDoubleNode.prev = temp
                    newDoubleNode.next = temp.next
                    temp.next = newDoubleNode
                    self.length += 1
                    return 0


    # 10 -- 29 -- 333 -- 32
    def remove(self, location):
        temp = self.head
        count = 0
        while(True):
            if location > self.length or location < 0:
                return print("Error: location should be within length: " + str(self.length))
            if(count != (location -1)):
                temp = temp.next
                count += 1
            else:
                temp2 = temp.next
                temp.next = temp2.next
                temp2.next.prev = temp
                temp2 = None
                self.length -= 1
                return 0


    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.value, end= ' ')
            temp = temp.next
        print()
        print('Length = ' + str(self.length))        


doubleLinkedList =  DoubleLinkedList()

doubleLinkedList.append(19)
doubleLinkedList.append(20)
doubleLinkedList.append(21)

doubleLinkedList.prepend(18)
doubleLinkedList.prepend(2)
doubleLinkedList.prepend(40)

doubleLinkedList.insert(214,3)
doubleLinkedList.insert(2324,3)
doubleLinkedList.insert(4,3)

doubleLinkedList.remove(3)

doubleLinkedList.printList()