class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[inf]*n for _ in range(n)]
        
        for city1, city2, dist in edges:
            distance[city1][city2] = dist
            distance[city2][city1] = dist
            
        for i in range(n):
            distance[i][i] = 0
            
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][via]+distance[via][j])
        
        smallest = defaultdict(list)
        for i in range(n):
            reachable = 0
            for j in range(n):
                if i == j:
                    continue
                if distance[i][j] <= distanceThreshold:
                    reachable += 1
            smallest[reachable].append(i)
        return smallest[min(smallest.keys())].pop()