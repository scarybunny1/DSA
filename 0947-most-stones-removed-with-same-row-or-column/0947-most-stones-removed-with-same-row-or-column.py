class DisjointSet:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
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
            return 1
        return 0
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        components = 0
        K = 10001
        ds = DisjointSet(2*K+1)
        seen = set()
        
        for i, j in stones:
            if i not in seen:
                seen.add(i)
                components += 1
            if j+K not in seen:
                seen.add(j+K)
                components += 1
        
        for i in range(len(stones)):
            x = stones[i][0]
            y = stones[i][1] + K
            
            components -= ds.union(x, y)
            
        return len(stones) - components