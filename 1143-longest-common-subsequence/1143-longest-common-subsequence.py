class Solution:
    def lcs(self, i, j, s1, s2, memo):
        if i == len(s1) or j == len(s2):
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s1[i] == s2[j]:
            memo[(i, j)] = 1 + self.lcs(i+1, j+1, s1, s2, memo)
        else:
            memo[(i, j)] = max(self.lcs(i+1, j, s1, s2, memo), self.lcs(i, j+1, s1, s2, memo))
        return memo[(i, j)]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def f(i, j):
#             if i < 0 or j < 0:
#                 return 0
            
#             if memo[i][j] == -1:
#                 if text1[i] == text2[j]:
#                     memo[i][j] = 1 + f(i-1, j-1)
#                 else:
#                     memo[i][j] = max(memo[i][j], f(i, j-1), f(i-1, j))
#             return memo[i][j]
        
#         memo = [[-1]* len(text2) for _ in range(len(text1))]
#         return f(len(text1)-1, len(text2)-1)
        memo = {}
        return self.lcs(0, 0, text1, text2, memo)
    
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        dp = [0]*(n+1)
        
        for i in range(1, m+1):
            temp = [0]*(n+1)
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    temp[j] = max(temp[j], dp[j], temp[j-1])
            dp = temp
        return dp[n]
                
                
                