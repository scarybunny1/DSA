class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        ans = 0
        length = 0
        while n:
            if length % 2:
                ans -= (n % 10)
            else:
                ans += (n % 10)
            n //= 10
            length += 1
        if length % 2 == 0:
            ans = -ans
        return ans