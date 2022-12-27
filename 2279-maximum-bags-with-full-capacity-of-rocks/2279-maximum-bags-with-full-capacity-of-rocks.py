class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        capacity = [capacity[i] - rocks[i] for i in range(n)]
        
        capacity.sort()
        
        a = additionalRocks
        bags_full = 0
        for c in capacity:
            if a < c:
                return bags_full
            a -= c
            bags_full += 1
        return bags_full