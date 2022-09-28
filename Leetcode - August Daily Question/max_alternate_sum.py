"""Given a list of integers, write a function that returns 
the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
 [5, 1, 1, 5] should return 10, since we pick 5 and 5"""

class Solution:
    def f(self, i, nums, memo):
        if i < 0:
            return 0

        if memo[i] == -1:
            take = nums[i] + self.f(i-2, nums, memo)
            not_take = self.f(i-1, nums, memo)

            memo[i] = max(take, not_take)

        return memo[i]

    def maxAlternateSum(self, nums) -> int:
        n = len(nums)
        memo = [-1] * n
        return self.f(n-1, nums, memo)


    def __init__(self, nums):
        self.nums = nums
        result = self.maxAlternateSum(self.nums)
        print(result)
    
if __name__ == "__main__":
    inp = [[2,4,6,2,5], [5, 1, 1, 5]]
    for _ in range(len(inp)):
        solution = Solution(inp[_])
