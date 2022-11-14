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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_island_area = 0
        ds = DisjointSet(n*m)
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                        adj_row, adj_col = row+dr, col+dc
                        if 0 <= adj_row < n and 0 <= adj_col < m and grid[adj_row][adj_col]:
                            node = row * m + col
                            adj_node = adj_row * m + adj_col
                            ds.union(node, adj_node)
                            
        componentSize = defaultdict(int)
        for i in range(n*m):
            parent_component = ds.find(i)
            componentSize[parent_component] += 1
            max_island_area = max(max_island_area, componentSize[parent_component])
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    neighbors = set()
                    for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                        adj_row, adj_col = row+dr, col+dc
                        if 0 <= adj_row < n and 0 <= adj_col < m and grid[adj_row][adj_col]:
                            adj_node = adj_row * m + adj_col
                            key = ds.find(adj_node)
                            neighbors.add(key)
                            
                    largeIslandArea = 1
                    for neighbor in neighbors:
                        largeIslandArea += componentSize[neighbor]
                        
                    max_island_area = max(max_island_area, largeIslandArea)
                            
        return max_island_area
                            
                            
                            
                            
                            
                            
                            