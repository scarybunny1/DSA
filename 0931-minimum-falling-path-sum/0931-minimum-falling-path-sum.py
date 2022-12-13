class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """Top Down DP - Recursive"""
#         def minPath(i, j):
#             if i == 0:
#                 return matrix[i][j]
#             if (i, j) not in memo:
#                 mini = minPath(i-1, j)
#                 if j > 0:
#                     mini = min(mini, minPath(i-1, j-1))
#                 if j < n - 1:
#                     mini = min(mini, minPath(i-1, j+1))
#                 memo[(i, j)] = mini + matrix[i][j]
#             return memo[(i, j)]
        
#         n = len(matrix)
#         mini = math.inf
#         memo = {}
#         for j in range(n):
#             mini = min(mini, minPath(n-1, j))
#         return mini
        """Bottom Up Iterative DP"""
        # n = len(matrix)
        # dp = matrix.copy()
        # for i in range(1, n):
        #     for j in range(n):
        #         mini = dp[i-1][j]
        #         if j > 0:
        #             mini = min(mini, dp[i-1][j-1])
        #         if j < n-1:
        #             mini = min(mini, dp[i-1][j+1])
        #         dp[i][j] += mini
        # mini = math.inf
        # for num in dp[n-1]:
        #     mini = min(mini, num)
        # return mini
        """Space Optimization"""
        n = len(matrix)
        dp = [num for num in matrix[0]]
        for i in range(1, n):
            temp = [0] * n
            for j in range(n):
                mini = dp[j]
                if j > 0:
                    mini = min(mini, dp[j-1])
                if j < n-1:
                    mini = min(mini, dp[j+1])
                temp[j] = mini + matrix[i][j]
            dp = temp
        mini = math.inf
        for num in dp:
            mini = min(mini, num)
        return mini
        
        
        