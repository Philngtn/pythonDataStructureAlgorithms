class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)

class Stack:
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def __str__(self):
        return str(self.__dict__)
    
    # Check the top element of the stack
    def peek(self):
        if (self.length == 0):
            return print("Stack Empty")
        return self.top.value
    
    def push(self, value):
        new_node = Node(value)

        if (self.length == 0):
            self.top = new_node
            self.bottom = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp

        self.length +=1

    def pop(self):
        if (self.length == 0):
            return print("Stack Empty")
    
        if (self.bottom == self.top):
            temp = self.top
            self.bottom = None
            self.top = None
            self.length -= 1
            return temp.value

        temp = self.top
        self.top = self.top.next
        self.length -=1

        return temp.value


class QueueUsingStacks:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.length = 0

    def peek(self):
        if (self.stack1.length == 0):
            return print("Queue empty using Peek")
        return print("Peek: ",self.stack1.peek())
    
    def enqueue(self, value):

        if (self.length == 0):
            self.stack1.push(value)
        else:
            while(self.stack1.length != 0):
                self.stack2.push(self.stack1.pop())

            self.stack1.push(value)

            while(self.stack2.length != 0):
                self.stack1.push(self.stack2.pop())

        self.length += 1
        return print("Enqueue :", value)
    
    def dequeue(self):
        if (self.stack1.length == 0):
            return print("Queue empty")
        self.length -= 1
        return print("Dequeue :",self.stack1.pop())


queue_by_stacks = QueueUsingStacks()

print("Adding Goolge and Tesla into the Queue: ")
queue_by_stacks.enqueue("Google")
queue_by_stacks.enqueue("Tesla")    

print("Showing the first element: ")
queue_by_stacks.peek()

print("Adding SpaceX into the queue: ")
queue_by_stacks.enqueue("SpaceX")

print("Pop 3 elements from the queue: ")
queue_by_stacks.dequeue()
queue_by_stacks.dequeue()
queue_by_stacks.dequeue()

print("Check empty queue: ")

queue_by_stacks.dequeue()
queue_by_stacks.peek()