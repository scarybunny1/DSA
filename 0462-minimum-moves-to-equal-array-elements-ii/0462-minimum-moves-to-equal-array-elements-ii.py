class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n//2]
        return sum(abs(x-median) for x in nums)