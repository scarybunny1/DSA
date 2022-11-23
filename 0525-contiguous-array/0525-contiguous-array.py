class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        d = {0:-1}
        maxi = 0
        curr_sum = 0
        for i in range(n):
            if nums[i] == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            
            if curr_sum in d:
                maxi = max(maxi, i - d[curr_sum])
            else:
                d[curr_sum] = i
        return maxi