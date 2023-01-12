class Solution:
    def dfs(self, r, c, grid, visited):
        n ,m = len(grid), len(grid[0])
        perimeter = 0
        for row, col in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
            if not (0 <= row < n and 0 <= col < m) or grid[row][col] == 0:
                perimeter += 1
                continue
            if grid[row][col] == 1 and (row, col) not in visited:
                visited.add((row, col))
                perimeter += self.dfs(row, col, grid, visited)
        return perimeter
        
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        n, m = len(grid), len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    perimeter += self.dfs(row, col, grid, visited)
        return perimeter