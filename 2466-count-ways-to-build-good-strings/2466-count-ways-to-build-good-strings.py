class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        ans = defaultdict(int)
        ans[0] = 1
        
        
        for i in range(1, high+1):
            ans[i] = (ans[i-one] + ans[i-zero]) % MOD
        
        count = 0
        for i in range(low, high+1):
            count = (count + ans[i]) % MOD
        return count