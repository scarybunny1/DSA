class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                point1 = points[i]
                point2 = points[j]
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges.append((distance, i, j))
        
        edges.sort()
        ds = DisjointSet(n)
        mst_sum = 0
        for weight, node1, node2 in edges:
            
            if ds.find(node1) != ds.find(node2):
                ds.union(node1, node2)
                mst_sum += weight
        return mst_sum
            
            
            
            
            