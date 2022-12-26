class Solution:
    def isPossible(self, t, prices, k):
        candies = []
        for price in prices:
            if not candies or candies[-1] + t <= price:
                candies.append(price)
        return len(candies) >= k
            
    def maximumTastiness(self, price: List[int], k: int) -> int:
        ans = 0
        price.sort()
        low, high = 0, price[-1]
        while low <= high:
            mid = (low+high)//2
            
            if self.isPossible(mid, price, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans