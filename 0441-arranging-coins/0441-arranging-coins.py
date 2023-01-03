class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        ans = -1
        while low <= high:
            k = (low + high) // 2
            
            coins = k * (k+1) // 2
            if coins <= n:
                ans = k
                low = k + 1
            else:
                high = k - 1
        return ans