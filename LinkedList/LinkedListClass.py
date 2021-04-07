class Node:
    def __init__(self, data):
        value = data
        next = None
         

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
            self.tail = newNode
            self.head.next = newNode
            self.length += 1

    def printList(self):
        temp = self.head
        while temp.next != None:
            print(temp.value, end= ' ')
            temp = temp.next
        print()
        print('Length =' + str(self.length))        

myLinkedList = LinkedList()
myLinkedList.append(22)
myLinkedList.printList()
