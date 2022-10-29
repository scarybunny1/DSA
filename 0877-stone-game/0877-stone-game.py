class Solution:
    def dp(self, left, right, piles, n, memo):
        if left > right:
            return 0
        
        if (left, right) in memo:
            return memo[(left, right)]
        piles_left = right - left + 1
        turn = piles_left % 2
        
        if turn == 0:
            memo[(left, right)] = max(piles[left] + self.dp(left+1, right, piles, n, memo), 
                       piles[right] + self.dp(left, right-1, piles, n, memo))
        else:
            memo[(left, right)] = min(-piles[left] + self.dp(left+1, right, piles, n, memo),
                       -piles[right] + self.dp(left, right-1, piles, n, memo))
        return memo[(left, right)]
        
    
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}
        return self.dp(0, n-1, piles, n, memo) > 0