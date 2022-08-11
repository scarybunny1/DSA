# 10th August, 2022
# Ayush S Bhatt

#108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which 
# the depth of the two subtrees of every node never differs by more than one.

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def bst(left, right):
            if right == left:
                return TreeNode(nums[left])
            elif right < left:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = bst(left, mid-1)
            node.right = bst(mid+1, right)
            return node
        return bst(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [1,2,5,8,11,21,33]
    print(Solution().sortedArrayToBST(nums))