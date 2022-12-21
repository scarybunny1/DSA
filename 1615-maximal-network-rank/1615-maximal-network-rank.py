class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = [0] * n
        graph = defaultdict(set)
        for x, y in roads:
            network[x] += 1
            network[y] += 1
            graph[x].add(y)
            graph[y].add(x)
        
        maxi = 0
        for first in range(n):
            for second in range(n):
                if first == second:
                    continue
                
                mnr = network[first] + network[second]
                mnr -= 1 if first in graph[second] else 0
                maxi = max(maxi, mnr)
        
        return maxi