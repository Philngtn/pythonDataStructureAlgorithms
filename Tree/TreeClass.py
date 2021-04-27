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
                # Check left node
                if (temp.left == None):
                    temp.left = new_node
                    return print("Add left", value)
                temp = temp.left
            else:
                # Check right node
                if (temp.right == None):
                    temp.right = new_node
                    return print("Add right", value)
                temp = temp.right



    def lookup(self, value):
        if (not self.root):
            return print("Empty")
        
        temp = self.root
        while(temp):
            if (value < temp.value):
                temp = temp.left
            elif (value > temp.value):
                temp = temp.right
            elif (value == temp.value):
                return temp
        
        return print("Found nothing")
            
    def remove(self,value):
        if (not self.root):
            return print("Empty Tree")
        
        if not self.lookup(value):
            return print("Node not found")
        
        parent_node = None
        current_node = self.root

        while(current_node):
            if(value < current_node.value):
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                # Option 1: No right child 
                if(current_node.right == None):
                    # Remove root node -> root node to the left
                    if(parent_node == None):
                        self.root = current_node.left
                    else:
                        # Left side, if parent > current value  
                        # make current LEFT child as parent's RIGHT child (NO RIGHT CHILD CASE) 
                        if (current_node.value < parent_node.value):
                            parent_node.left = current_node.left
                        # Left side, if parent < current value  
                        # make current LEFT child as parent's RIGHT child (NO RIGHT CHILD CASE)
                        elif (current_node.value > parent_node.value):
                            parent_node.right = current_node.left
                            
                # Option 2: Right child does't have a left child 
                elif (current_node.right.left == None):
                    if (parent_node == None):


                    


    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
           # Recusion print all left nodes 
           self.printt(curr_node.left)
           print(str(curr_node.value))
           # Recusion print all right nodes
           self.printt(curr_node.right)

tree = BinarySeachTree()

tree.insert(43)
tree.insert(20)
tree.insert(650)
tree.insert(34)
tree.insert(40)

print(tree.lookup(34))

tree.print_tree()