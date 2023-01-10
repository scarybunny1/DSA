class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        d = defaultdict(int)
        for num in nums:
            square = num*num
            if square in d:
                d[num] = d[square] + 1
            else:
                d[num] = 1
        ans = max(d.values())
        return -1 if ans < 2 else ans