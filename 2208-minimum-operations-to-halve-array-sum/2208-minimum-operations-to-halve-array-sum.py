class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)
        total = sum(nums)
        steps = 0
        half = total / 2
        print(total, half)
        while total > half:
            largest = -heapq.heappop(pq)
            largest /= 2
            total -= largest
            steps += 1
            heapq.heappush(pq, -largest)
        return steps