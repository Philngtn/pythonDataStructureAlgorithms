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
                        # Right side, if parent < current value  
                        # make current LEFT child as parent's RIGHT child (NO RIGHT CHILD CASE)
                        elif (current_node.value > parent_node.value):
                            parent_node.right = current_node.left
                    
                # Option 2: Right child does't have a left child 
                elif (current_node.right.left == None):
                    current_node.right.left = current_node.left
                    if (parent_node == None):
                        # Take left node as the root node 
                        self.root = current_node.left
                    else:
                        # Take the left empty space of the child (Option 2)
                        #  and put the LEFT node of current node
                        
                        # Left side, make right child of the left parent
                        if (current_node.value < parent_node.value):
                            parent_node.left = current_node.right
                        # 
                        elif (current_node.value > parent_node.value):
                            parent_node.right = current_node.right
                
                # Option 3: Right child that has a left child 
                else:
                    # Find the Right child's left most child
                    leftMost = current_node.right.left
                    leftMostParent = current_node.right
                    while (leftMost.left != None ):
                        leftMostParent = leftMost
                        leftMost = leftMost.left

                    leftMostParent.left = leftMost.right
                    leftMost.left = current_node.left
                    leftMost.right = current_node.right

                    if (parent_node == None):
                        self.root = leftMost
                    else:
                        if(current_node.value < parent_node.value):
                            parent_node.left = leftMost
                        elif (current_node.value > parent_node.value):
                            parent_node.right = leftMost

                
                return True

# InOrder - [1,4,6,9,15,20,170]
# PreOrder - [9,4,1,6,20,15,170]
# PostOrder - [1,6,4,15,170,20,9]
#                  9
#          4              20
#      1      6       15       170

    def traverse_InOrder(self, node, list_node):
        # Searching left node
        if node.left:
            self.traverse_InOrder(node.left , list_node)
        # if not have left node, add to the list
        list_node.append(node.value)
        # Check whether the current node has a right node -> call the function to seach the 
        # left node in this current right node 
        if node.right:
            self.traverse_InOrder(node.right , list_node)
        # If does not have any branch -> return the list
        return list_node

    def traverse_PreOrder(self, node, list_node):
        list_node.append(node.value)
        if node.left:
            self.traverse_PreOrder(node.left, list_node)
        if node.right:
            self.traverse_PreOrder(node.right, list_node)
        return list_node
    
    def traverse_PostOrder(self, node, list_node):
        if node.left:
            self.traverse_PostOrder(node.left, list_node)
        if node.right:
            self.traverse_PostOrder(node.right, list_node)
        list_node.append(node.value)
        return list_node

    def DepthFirstSearch_InOrder(self):
        return print(self.traverse_InOrder(self.root, []))

    def DepthFirstSearch_PreOrder(self):
        return print(self.traverse_PreOrder(self.root, []))

    def DepthFirstSearch_PostOrder(self):
        return print(self.traverse_PostOrder(self.root, []))


tree = BinarySeachTree()

tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)

tree.DepthFirstSearch_InOrder()
tree.DepthFirstSearch_PreOrder()
tree.DepthFirstSearch_PostOrder()
