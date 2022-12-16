# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, node, curr_sum, target, d):
        if not node:
            return 0
            
        curr_sum += node.val
        cnt = 0
        
        #Path from root to current node
        if curr_sum == target:
            cnt += 1
        
        #Some intermediate path
        if curr_sum - target in d:
            cnt += d[curr_sum - target]
        
        #Storing prefix formed till now
        d[curr_sum] = d.get(curr_sum, 0) + 1
        
        #Continuing to the child nodes
        cnt += self.count(node.left, curr_sum, target, d)
        cnt += self.count(node.right, curr_sum, target, d)
        
        d[curr_sum] = d.get(curr_sum, 0) - 1
        
        return cnt
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = {}
        return self.count(root, 0, targetSum, d)