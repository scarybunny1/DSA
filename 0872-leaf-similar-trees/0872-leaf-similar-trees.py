# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafSequence(self, node, res):
        if not node:
            return
        
        if node.left is None and node.right is None:
            res.append(node.val)
            return
        
        self.getLeafSequence(node.left, res)
        self.getLeafSequence(node.right, res)
        
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        
        self.getLeafSequence(root1, seq1)
        self.getLeafSequence(root2, seq2)
        
        return seq1 == seq2