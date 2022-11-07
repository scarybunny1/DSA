class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        graph = defaultdict(list)
        for city, neighbor_city, time in roads:
            graph[city].append((neighbor_city, time))
            graph[neighbor_city].append((city, time))
        
        heap = [(0, 0)]
        distance = [inf]*n
        distance[0] = 0
        ways = [0]*n
        ways[0] = 1
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            for neighbor, d in graph[node]:
                if dist + d == distance[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
                if dist + d < distance[neighbor]:
                    distance[neighbor] = d + dist
                    heapq.heappush(heap, (distance[neighbor], neighbor))
                    ways[neighbor] = ways[node]
            
        return ways[n-1]