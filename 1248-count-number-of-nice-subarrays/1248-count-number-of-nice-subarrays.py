class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] % 2
        
        d = {0:1}
        nice = 0
        curr_sum = 0
        
        for i in range(n):
            curr_sum += nums[i]
            
            if curr_sum - k in d:
                nice += d[curr_sum-k]
            
            d[curr_sum] = d.get(curr_sum, 0) + 1
        
        return nice