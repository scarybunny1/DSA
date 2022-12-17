class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        left = 0
        curr_sum = 0
        mini_len = len(nums)
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                mini_len = min(mini_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        return mini_len