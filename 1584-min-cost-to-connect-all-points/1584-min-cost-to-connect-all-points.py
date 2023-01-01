class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False
                
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        ds = DisjointSet(n)
        pq = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                pq.append((dist, i, j))
        heapq.heapify(pq)
        cost = 0
        while pq:
            dist, x, y = heapq.heappop(pq)
            if ds.union(x, y):
                cost += dist
        return cost
            
            
            
            
            