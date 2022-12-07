# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, node, overall_max):
        if not node:
            return 0, -inf
        
        left_sum, overall_max_left = self.path(node.left, overall_max)
        right_sum, overall_max_right = self.path(node.right, overall_max)
        
        overall_max = max(overall_max_left, overall_max_right, node.val + max(0, left_sum) + max(0, right_sum))
        
        return node.val + max(0, left_sum, right_sum), overall_max
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.path(root, -inf))