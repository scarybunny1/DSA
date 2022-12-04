class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        min_abs_diff = inf
        total = sum(nums)
        index = 0
        for i in range(n-1):
            prefix += nums[i]
            left = prefix // (i + 1)
            right = (total - prefix) // (n - i - 1)
            if min_abs_diff > abs(left - right):
                index = i
                min_abs_diff = abs(left-right)
        if (total // n) < min_abs_diff:
            index = n-1
        return index