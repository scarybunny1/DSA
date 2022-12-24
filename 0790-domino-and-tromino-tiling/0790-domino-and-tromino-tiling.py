class Solution:
    def numTilings(self, n: int) -> int:
        # dp[i] = dp[i-1] * 2 + dp[i-3]
        # 1 = 1   1 * 2
        # 2 = 2   2 * 2 + 1
        # 3 = 5   5 * 2 + 1
        # 4 = 11  11 * 2 + 2
        # 5 = 24  24 * 2 + 5
        # 6 = 53  53 * 2 + 11
        # 7 = 117 117 * 2 + 24
        # 8 = 258
        # 9 = 569
        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (2 * dp[i-1]) % MOD
            
            if i-3 >= 0:
                dp[i] = (dp[i] + dp[i-3]) % MOD
        return dp[n]
    