class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # 1:02:30
        pq = []
        
        for pile in piles:
            heapq.heappush(pq, -pile)
            
        while k > 0:
            highest = -heapq.heappop(pq)
            heapq.heappush(pq, -(highest - highest // 2))
            k -= 1
        
        return sum(-value for value in pq)