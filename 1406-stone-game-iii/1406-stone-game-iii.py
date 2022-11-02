class Solution:
    def dp(self, i, player, nums, n, memo):
        if i == n:
            return 0
        if (i, player) not in memo:
            if player == 0:
                take_two = take_three = -inf
                take_one = nums[i] + self.dp(i+1, player ^ 1, nums, n, memo)
                if i + 1 < n:
                    take_two = nums[i] + nums[i+1] + self.dp(i+2, player ^ 1, nums, n, memo)
                if i + 2 < n:
                    take_three = nums[i] + nums[i+1] + nums[i+2] + self.dp(i+3, player ^ 1, nums, n, memo)
                memo[(i, player)] = max(take_one, take_two, take_three)
            else:
                take_two = take_three = inf
                take_one = -nums[i] + self.dp(i+1, player ^ 1, nums, n, memo)
                if i + 1 < n:
                    take_two = -nums[i] - nums[i+1] + self.dp(i+2, player ^ 1, nums, n, memo)
                if i + 2 < n:
                    take_three = -nums[i] - nums[i+1] - nums[i+2] + self.dp(i+3, player ^ 1, nums, n, memo)
                memo[(i, player)] = min(take_one, take_two, take_three)
        return memo[(i, player)]
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        result = self.dp(0, 0, stoneValue, len(stoneValue), memo)
        if result == 0:
            return "Tie"
        elif result < 0:
            return "Bob"
        return "Alice"