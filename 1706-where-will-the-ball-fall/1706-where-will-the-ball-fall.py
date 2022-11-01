class Solution:
    def isSafe(self, col, m):
        return (0 <= col < m)
        
    def dfs(self, row, col, grid, n, m):
        if not self.isSafe(col, m):
            return -1
        
        if row == n:
            return col
        
        adj_col = grid[row][col] + col
        if self.isSafe(adj_col, m) and grid[row][col] + grid[row][adj_col] == 0:
            return -1
        
        return self.dfs(row+1, adj_col, grid, n, m)
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        
        res = [-1] * m
        for col in range(m):
            res[col] = self.dfs(0, col, grid, n, m)
    
        return res