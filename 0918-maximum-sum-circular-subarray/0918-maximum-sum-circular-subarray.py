class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         1 -2 3 -2
#         1 -1 3 -1
        
#         5 -3 5
#         5  2 7
        
#         -3 -2 -3
#         -3 -2 -3
        
        
#         x1 x2 x3 x4 x5 x6
        
        
        total = sum(nums)
        min_sum = max_sum = nums[0]
        curr_minsum = curr_maxsum = 0
        for num in nums:
            curr_minsum = min(num, curr_minsum + num)
            min_sum = min(curr_minsum, min_sum)
            
            curr_maxsum = max(num, curr_maxsum + num)
            max_sum = max(max_sum, curr_maxsum)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum