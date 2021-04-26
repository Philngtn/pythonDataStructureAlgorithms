from typing import NoReturn


class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):  
        return str(self.__dict__)


class BinarySeachTree:

    def __init__(self):
        self.root = None

        
    def __str__(self):  
        return str(self.__dict__)

    def insert(self, value):
        new_node = Node(value)

        if(self.root == None):
            self.root = new_node
            return print("Add root", value)
        
        temp = self.root

        while(True):
            if(value < temp.value):
                if (temp.left == None):
                    temp.left = new_node
                    return print("Add left", value)
                else:
                    temp = temp.left

            elif(value >= temp.value):
                if (temp.right == None):
                    temp.right = new_node
                    return print("Add right", value)
                else:
                    temp = temp.right



    def lookup(self):
        pass

    def remove(self):
        pass
    
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
           self.printt(curr_node.left)
           print(str(curr_node.value))
           self.printt(curr_node.right)

tree = BinarySeachTree()

tree.insert(43)
tree.insert(20)
tree.insert(650)
tree.insert(34)
tree.insert(40)

tree.print_tree()