class Solution:
    def findPath(self, row, col, squares, grid, visited):
        n, m = len(grid), len(grid[0])
        if squares == 1 and grid[row][col] == 2:
            return 1
        
        squares -= 1
        visited.add((row, col))
        
        ans = 0
        for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
            r, c = row+dr, col+dc
            if not (0 <= r < n and 0 <= c < m and grid[r][c] != -1 and (r, c) not in visited):
                continue
            ans += self.findPath(r, c, squares, grid, visited)
            
        visited.remove((row, col))
        squares += 1
        
        return ans
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        clear_squares = 0
        start_row, start_col = 0, 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    clear_squares += 1
                if grid[i][j] == 1:
                    start_row, start_col = i, j
        
        return self.findPath(start_row, start_col, clear_squares, grid, set())