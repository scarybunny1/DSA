class Solution:
    def findSum(self, i, target, nums, memo):
        if i == len(nums):
            if target == 0:
                return 1
            return 0
        
        if (i, target) in memo:
            return memo[(i, target)]
        
        take = 0
        if nums[i] <= target:
            take = self.findSum(i+1, target-nums[i], nums, memo)
        not_take = self.findSum(i+1, target, nums, memo)
    
        memo[(i, target)] = take + not_take
        return memo[(i, target)]
        
        
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k:
            return 0
        n = len(nums)
        MOD = 10**9 + 7
        total = 2**n
        invalid = 0
        memo = {}
        for target in range(k):
            invalid += self.findSum(0, target, nums, memo)
        
        return max(total - 2*invalid, 0) % MOD