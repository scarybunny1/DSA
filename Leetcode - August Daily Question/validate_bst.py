#11th August, 2022
#Ayush S Bhatt

#98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def validateBST(self, node, left, right):
        #Check if node is not null
        if node is None:
            return True
        #Check if current node's value is in correct range
        return ((left < node.val < right) and 
                self.validateBST(node.left, left, min(right, node.val)) and #Update right range for the left child
                self.validateBST(node.right, max(left, node.val), right)) #Update left range for the right child

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().validateBST(root, -math.inf, math.inf))
    