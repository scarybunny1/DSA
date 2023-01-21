class Solution:
    def check(self, r, c, valid, grid, memo):
        n = len(grid)
        m = len(grid[0])
        
        if (r, c, valid) in memo:
            return memo[(r, c, valid)]
        
        if (r, c) == (n-1, m-1):
            return valid == 0
        
        for row, col in (r+1, c), (r, c+1):
            if row >= n or col >= m or valid < 0:
                continue
                
            if grid[row][col] == '(':
                valid += 1
            else:
                valid -= 1
                
            if self.check(row, col, valid, grid, memo):
                return True
            
            if grid[row][col] == '(':
                valid -= 1
            else:
                valid += 1
            
        memo[(r,c,valid)] = False
            
            
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        if grid[0][0] == ')' or grid[n-1][m-1] == '(':
            return False
        
        return self.check(0, 0, 1, grid, {})