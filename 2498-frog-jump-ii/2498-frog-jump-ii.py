class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        ans = stones[1] - stones[0]
        
        for i in range(2, n, 2):
            ans = max(ans, stones[i] - stones[i-2])
        for i in range(3, n, 2):
            ans = max(ans, stones[i] - stones[i-2])
                
        return ans