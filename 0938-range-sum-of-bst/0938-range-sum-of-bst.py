# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSum(self, node, low, high):
        if not node:
            return 0
        
        ans = 0
        
        if low <= node.val <= high:
            ans += node.val
            
        if node.val >= low:
            ans += self.rangeSum(node.left, low, high)
        
        if node.val <= high:
            ans += self.rangeSum(node.right, low, high)
            
        return ans
        
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.rangeSum(root, low, high)