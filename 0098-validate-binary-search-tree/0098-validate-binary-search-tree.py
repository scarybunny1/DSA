# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            return left < node.val < right and validate(node.left, left, min(right, node.val)) and validate(node.right, max(left, node.val), right)
        
        return validate(root, -math.inf, math.inf)
            