# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 3: Linked List
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
    
    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self,value):
        newNode = Node(value)

        if (self.length == 0):    
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        
        if (self.length == 0):    
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    def insert(self, value, location):
        newNode = Node(value)
        temp = self.head
        count = 0
        
        if (self.length == 0):    
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return 0


        while (True):
            if location > self.length:
                self.append(value)
                break
            elif location == 0:
                self.prepend(value)
                break
            else:
                if (count != (location - 1)):
                    temp = temp.next 
                    count += 1                           
                else:
                    newNode.next = temp.next
                    temp.next = newNode
                    self.length +=1
                    return 0
    
    def remove(self,location):
        temp = self.head
        count = 0
        while(True):
            if location > self.length or location < 0:
                return print("Error: location should be within length: " + str(self.length))
            if (count != (location-1)):
                temp = temp.next
                count += 1
            else:
                temp2 = temp.next
                temp.next = temp2.next 
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

myLinkedList = LinkedList()

myLinkedList.append(22)
myLinkedList.append(223)
myLinkedList.append(221)

myLinkedList.prepend(2123)
myLinkedList.prepend(88)
myLinkedList.prepend(53)

myLinkedList.insert(1,22)
myLinkedList.insert(42,0)
myLinkedList.insert(1,4)

myLinkedList.remove(4)
myLinkedList.remove(99)

myLinkedList.printList()

