class Solution:
    def canFormSum(self, i, target, nums, memo):
        if target < 0:
            return False
        
        if i == len(nums):
            if target == 0:
                return True
            return False
        
        if (i, target) in memo:
            return memo[(i, target)]
        
        take = self.canFormSum(i+1, target-nums[i], nums, memo)
        not_take = self.canFormSum(i+1, target, nums, memo)
        
        memo[(i, target)] = take or not_take
        return memo[(i, target)]
        
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        return self.canFormSum(0, total//2, nums, {})