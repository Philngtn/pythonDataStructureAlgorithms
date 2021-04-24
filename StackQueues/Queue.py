class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0


    def peek(self):
        if(self.length == 0):
            return print("Empty queue with peek !!!")
        return print(self.first.value)
    
    def enqueue(self, value):
        
        new_node = Node(value)
        
        if(self.length == 0):
            self.first = new_node
            self.last = new_node
        else:
            pointer = self.last
            self.last = new_node
            pointer.next = new_node

        self.length +=1

        return print("Enqueue :", value)

    def dequeue(self):
        if (self.length == 0):
            return print("Empty queue !!!")
        
        if (self.first == self.last):
            pointer = self.first
            self.first = None
            self.last = None
            self.length -= 1
            return print("Dequeue :", pointer.value)
        
        pointer = self.first.next
        dequeue_value = self.first
        self.first = pointer
        self.length -=1

        return print("Dequeue :",dequeue_value.value)

new_queue = Queue()


print("Adding Goolge and Testla into the Queue: ")
new_queue.enqueue("Google")
new_queue.enqueue("Tesla")    

print("Showing the first element: ")
new_queue.peek()

print("Adding SpaceX into the queue: ")
new_queue.enqueue("SpaceX")

print("Pop 3 elements from the queue: ")
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()

print("Check empty queue: ")

new_queue.dequeue()
new_queue.peek()