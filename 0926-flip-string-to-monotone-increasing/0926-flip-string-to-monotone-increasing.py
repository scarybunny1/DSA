class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroes = 0
        for c in s:
            if c == '0':
                zeroes += 1
        
        ans = zeroes
        
        for c in s:
            if c == '0':
                zeroes -= 1
                ans = min(ans, zeroes)
            else:
                zeroes += 1
        
        return ans