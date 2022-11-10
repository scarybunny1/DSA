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
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1                

class Solution:
    def find_mst_with_edge(self, i, edges, n):
        mst_inc = 0
        ds = DisjointSet(n)
        edge = edges[i]
        ds.union(edge[0], edge[1])
        mst_inc += edge[2]
        
        for eno, (x, y, weight, _) in enumerate(edges):
            if eno == i:
                continue
            if ds.find(x) != ds.find(y):
                ds.union(x, y)
                mst_inc += weight
        parent = ds.find(0)
        return mst_inc if all(ds.find(i) == parent for i in range(n)) else inf
    
    def find_mst_without_edge(self, i, edges, n):
        ds = DisjointSet(n)
        mst_exc = 0
        
        for eno, (x, y, weight, _) in enumerate(edges):
            if eno == i:
                continue
            if ds.find(x) != ds.find(y):
                ds.union(x, y)
                mst_exc += weight
        parent = ds.find(0)
        return mst_exc if all(ds.find(i) == parent for i in range(n)) else inf
        
    
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(node, neighbor, weight, i) for i, (node, neighbor, weight) in enumerate(edges)]
        edges.sort(key= lambda x: x[2])
        ds = DisjointSet(n)
        mst_base_sum = 0
        for x, y, weight, _ in edges:
            if ds.find(x) != ds.find(y):
                ds.union(x, y)
                mst_base_sum += weight
        
        critical = set()
        pcritical = set()
        for i in range(len(edges)):
            edge = edges[i]
            if self.find_mst_without_edge(i, edges, n) > mst_base_sum:
                critical.add(edge[3])
            elif self.find_mst_with_edge(i, edges, n) == mst_base_sum:
                pcritical.add(edge[3])
                    
        return [critical, pcritical]
        
        
        
        
        