class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [0]*(n+1)
        dp[0] = 1
        MOD = 10**9+7
        for i in range(1, n+1):
            dp[i] += dp[i-1]
            if i > 1 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i-2]
                if i > 2 and pressedKeys[i-1] == pressedKeys[i-3]:
                    dp[i] += dp[i-3]
                    if i > 3 and pressedKeys[i-1] in "79" and pressedKeys[i-1] == pressedKeys[i-4]:
                        dp[i] += dp[i-4]
            dp[i] %= MOD
        return dp[n]