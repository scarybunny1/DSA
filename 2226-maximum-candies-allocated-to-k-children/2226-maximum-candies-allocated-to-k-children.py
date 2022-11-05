class Solution:
    def getWholeCandyPile(self, candy_cnt, candies):
        piles = 0
        
        for candy in candies:
            piles += candy // candy_cnt
        
        return piles
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        ans = -1
        left, right = 1, max(candies)
        while left <= right:
            mid = (left + right) // 2
            
            if self.getWholeCandyPile(mid, candies) >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans