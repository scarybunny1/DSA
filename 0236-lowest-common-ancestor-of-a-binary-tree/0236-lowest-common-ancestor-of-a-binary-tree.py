# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca(self, node, p, q):
        if not node:
            return False
        if node.val == p or node.val == q:
            return True
        
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        current = node == p or node == q
        
        if left + right + current > 1:
            self.ans = node
        
        return left or right or current
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca(root, p, q)
        return self.ans