class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.size[rootX] > self.size[rootY]:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.root[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        
        for x, y in edges:
            ds.union(x, y)
            
        pairs = 0
        print(ds.root, ds.size)
        for node in range(n):
            if node == ds.root[node]:
                component_size = ds.size[node]
                pairs += component_size * (n - component_size)
        return pairs // 2
        