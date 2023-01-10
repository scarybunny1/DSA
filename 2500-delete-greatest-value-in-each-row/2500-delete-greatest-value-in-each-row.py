class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            grid[i].sort()
            
        ans = 0
        for col in range(m):
            maxi = 0
            for row in range(n):
                maxi = max(maxi, grid[row][col])
            ans += maxi
        return ans