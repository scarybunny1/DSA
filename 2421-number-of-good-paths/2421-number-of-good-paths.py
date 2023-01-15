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
        
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        values = defaultdict(list)
        for i, val in enumerate(vals):
            values[val].append(i)
        
        ds = DisjointSet(len(vals))
        good_paths = 0
        
        for value, nodes in sorted(values.items()):
            for node in nodes:
                for nei in graph[node]:
                    if vals[nei] <= value:
                        ds.union(node, nei)
            component = defaultdict(int)
            for node in nodes:
                parent = ds.find(node)
                component[parent] += 1
            good_paths += sum(x*(x+1)//2 for x in component.values())
        return good_paths
                        
                        
                        