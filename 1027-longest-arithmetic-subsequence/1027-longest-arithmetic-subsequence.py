class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                if (i, diff) not in dp:
                    dp[(i, diff)] = 1
                dp[(j, diff)] = dp[(i, diff)] + 1
        return max(dp.values())