class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = mid = 0
        for x in count.values():
            if x % 2 == 0:
                res += x
            else:
                res += x - 1
                mid = 1
        return res + mid