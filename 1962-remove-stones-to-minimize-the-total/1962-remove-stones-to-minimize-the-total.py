class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Start time: 1:02:30
        # End time:   1:08:15
        # Time to solve question on first attempt: 5 mins 45 seconds.
        pq = [-pile for pile in piles]
        
        heapq.heapify(pq)
            
        while k > 0:
            highest = -heapq.heappop(pq)
            heapq.heappush(pq, -(highest - highest // 2))
            k -= 1
        
        return sum(-value for value in pq)