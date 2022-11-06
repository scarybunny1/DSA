class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        left, right = min(candidates-1, n), max(n-candidates, 0)
        group = []
        if left < right:
            group += [(costs[i], i) for i in range(left+1)]
            group += [(costs[i], i) for i in range(right, n)]
        else:
            group += [(cost, i) for i, cost in enumerate(costs)]
            
        heapq.heapify(group)
        total_cost = 0
        for _ in range(k):
            cost, index = heapq.heappop(group)
            total_cost += cost
            
            if left + 1 < right:
                if index <= left:
                    left += 1
                    heapq.heappush(group, (costs[left], left))
                elif index >= right:
                    right -= 1
                    heapq.heappush(group, (costs[right], right))
        return total_cost
    
