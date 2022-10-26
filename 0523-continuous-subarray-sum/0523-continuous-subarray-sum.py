class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = {0:0}
        curr_sum = 0
        n = len(nums)
        for i in range(n):
            curr_sum += nums[i]
            
            if curr_sum % k not in s:
                s[curr_sum % k] = i + 1
            elif s[curr_sum % k] < i:
                return True
        return False