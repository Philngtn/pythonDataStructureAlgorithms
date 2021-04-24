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
            self.length += 1
        else:
            temp = self.top
            self.top = new_node
            temp.next = new_node
            self.length += 1

    def pop(self):
        temp = self.bottom

        if(self.length == 0):
            return print("Empty stack")

        if(temp == self.top):
            self.length -= 1
            self.top = None
            self.bottom = None
            return print(temp.value)

        while(True):
            if(temp.next != self.top):
                temp = temp.next
            else:
                return_value = temp.next
                self.top = temp
                self.length -= 1
                return print(return_value.value)
        



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
