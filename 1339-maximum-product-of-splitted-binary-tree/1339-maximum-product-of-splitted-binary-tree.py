# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateTotal(self, node):
        if not node:
            return 0
        
        sum = node.val
        sum += self.calculateTotal(node.left)
        sum += self.calculateTotal(node.right)
        
        return sum
        
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        MOD = 10**9 + 7
        total = self.calculateTotal(root)
        self.sumAtNode(root, maxi, total)
        return maxi[0] % MOD
    
    def sumAtNode(self, node, maxi, total):
        if not node:
            return 0
        
        sum = node.val
        sum += self.sumAtNode(node.left, maxi, total)
        sum += self.sumAtNode(node.right, maxi, total)
        
        maxi[0] = max(maxi[0], sum * (total - sum))
        
        return sum
    
    
    