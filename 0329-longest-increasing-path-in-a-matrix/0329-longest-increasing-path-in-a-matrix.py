class Solution:
    def dfs(self, row, col, matrix, memo):
        n, m = len(matrix), len(matrix[0])
        if memo[row][col] == -1:
            increasing = 1
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                if (0 <= row+dx < n and 0 <= col+dy < m and matrix[row][col] < matrix[row+dx][col+dy]):
                     increasing = max(increasing, 1 + self.dfs(row+dx, col+dy, matrix, memo))
            memo[row][col] = increasing
        return memo[row][col]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        memo = [[-1]*m for _ in range(n)]
        max_inc_path = 1
        for row in range(n):
            for col in range(m):
                max_inc_path = max(max_inc_path, self.dfs(row, col, matrix, memo))
        return max_inc_path