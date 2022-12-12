class Solution:
    def climbStairs(self, n: int) -> int:
#         def climbWays(i):
#             if i <= 2:
#                 return i
            
#             if memo[i] == -1:
#                 memo[i] = climbWays(i-1) + climbWays(i-2)
#             return memo[i]
        
#         memo = [-1] * (n+1)
#         return climbWays(n)

        one_step = two_step = 1
        for i in range(2, n+1):
            one_step, two_step = two_step, one_step + two_step
        return two_step