class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Total is sum upto n+1
        #Current sum is sum(nums)
        #Missing number is Total - Current
        n = len(nums)
        total = n*(n+1)//2
        current_sum = sum(nums)
        return total - current_sum