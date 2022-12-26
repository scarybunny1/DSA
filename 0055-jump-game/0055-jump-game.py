class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        possible = n-1
        for i in range(n-2, -1, -1):
            if i+nums[i] >= possible:
                possible = i
        return possible == 0