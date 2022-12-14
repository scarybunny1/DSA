class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, x):
        if x == self.root[x]:
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
                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        for edge in edges[::-1]:
            ds = DisjointSet(n+1)
            
            for e in edges:
                if e == edge:
                    continue
                
                ds.union(e[0], e[1])
            
            components = sum(1 for root, node in enumerate(ds.root) if root == node)
            if components == 2:
                return edge
        
        return []