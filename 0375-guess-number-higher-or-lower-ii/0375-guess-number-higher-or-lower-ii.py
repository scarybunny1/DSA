class Solution:
    def dp(self, left, right, memo):
        if left >= right:
            return 0
        
        if memo[left][right] != -1:
            return memo[left][right]
        
        ans = inf
        for pick in range(left, right+1):
            leftCost = self.dp(left, pick - 1, memo)
            rightCost = self.dp(pick + 1, right, memo)
            ans = min(ans, max(leftCost, rightCost) + pick)
        memo[left][right] = ans
        
        return ans
    
    def getMoneyAmount(self, n: int) -> int:

        # 1 2 3 4  5  6  7  8  9  10
        # 1 3 6 10 15 21 28 36 45 55
        # l
        #                         h
        #                 m
        memo = [[-1]*(n+1) for _ in range(n+1)]
        return self.dp(1, n, memo)