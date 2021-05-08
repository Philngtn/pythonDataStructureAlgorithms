# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode):
        list_node = []
        i = 1
        list_node = self.traverse_inorder(root, list_node)
        while i < len(list_node):
            if(list_node[i] <= list_node[i - 1]):
                return False
            i += 1
    
        return True
    
    
    def traverse_inorder(self, node, list_node):
        if node.left:
            self.traverse_inorder(node.left, list_node)
        list_node.append(node.val)
        if node.right:
            self.traverse_inorder(node.right, list_node)
        return list_node
        