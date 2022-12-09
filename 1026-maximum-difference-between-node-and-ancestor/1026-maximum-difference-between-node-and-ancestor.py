# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDiff(self, node, mini, maxi):
        if not node:
            return 0
        
        mini = min(mini, node.val)
        maxi = max(maxi, node.val)
        ans = maxi - mini
        
        return max(ans, self.getMaxDiff(node.left, mini, maxi), self.getMaxDiff(node.right, mini, maxi))
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDiff(root, root.val, root.val)