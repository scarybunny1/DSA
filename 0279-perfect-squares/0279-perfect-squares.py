class Solution:
    def count(self, n, memo):
        if n == 0:
            return 0
        
        if n < 0:
            return inf
        
        if memo[n] != -1:
            return memo[n]
        
        i = 1
        mini = n
        
        while i*i <= n:
            mini = min(mini, 1 + self.count(n - (i*i), memo))
            i += 1
        memo[n] = mini
        
        return memo[n]
    
    def numSquares(self, n: int) -> int:
        # memo = [-1] * (n+1)
        # return self.count(n, memo)
    
        dp = [inf] * (n+1)
        dp[0] = 0
        for j in range(1, n+1):
            i = 1
            while i*i <= j:
                dp[j] = min(dp[j], 1 + dp[j-(i*i)])
                i += 1
        return dp[n]