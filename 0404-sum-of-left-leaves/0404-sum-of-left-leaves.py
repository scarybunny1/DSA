# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateSum(self, node, isLeftChild):
        if not node:
            return 0
        if isLeftChild and node.left is None and node.right is None:
            return node.val
        left = self.calculateSum(node.left, True)
        right = self.calculateSum(node.right, False)
        total = left + right
        
        return total
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.calculateSum(root, False)