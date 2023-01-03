# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def paths(self, node, total, target, d):
        if not node:
            return 0
        
        ans = 0
        
        total += node.val
        #Starting from root
        if total == target:
            ans += 1
        
        #Starting from intermediate node
        if total - target in d:
            ans += d[total-target]
            
        d[total] = d.get(total, 0) + 1
        ans += self.paths(node.left, total, target, d)
        ans += self.paths(node.right, total, target, d)
        d[total] = d.get(total, 0) - 1
        
        return ans
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = {}
        
        return self.paths(root, 0, targetSum, d)