class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # 16 8 6 4 3 2
        d = {}
        ans = 0
        for num in nums:
            square = num * num
            if square in d:
                d[num] = d[square] + 1
                ans = max(ans, d[num])
            else:
                d[num] = 1
        return -1 if ans < 2 else ans