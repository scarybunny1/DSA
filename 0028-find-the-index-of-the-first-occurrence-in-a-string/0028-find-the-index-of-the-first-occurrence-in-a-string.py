class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(0, m - n + 1):
            if needle == haystack[i:i+n]:
                return i
        return -1