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
        return print(self.top.value)
    
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
        return print(new_node.value)   

    def pop(self):
        if (self.length == 0):
            return print("Stack Empty")
    
        if (self.bottom == self.top):
            temp = self.top
            self.bottom = None
            self.top = None
            self.length -= 1
            return print(temp.value)

        temp = self.top
        self.top = self.top.next
        self.length -=1

        return print(temp.value)



newStack = Stack()

print("Adding Goolge and Testla into the stack: ")
newStack.push("Google")
newStack.push("Tesla")    

print("Showing the top element: ")
newStack.peek()

print("Adding SpaceX into the stack: ")
newStack.push("SpaceX")

print("Pop 3 elements from the stack: ")
newStack.pop()
newStack.pop()
newStack.pop()
