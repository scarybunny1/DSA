# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        if left_depth == right_depth:
            return int(2 ** left_depth) + self.countNodes(root.right)
        else:
            return int(2 ** right_depth) + self.countNodes(root.left)