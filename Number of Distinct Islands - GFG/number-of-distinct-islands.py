#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        visited = set()
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    shape = []
                    self.floodfill(i, j, shape, (i,j), grid, visited)
                    islands.add(tuple(sorted(shape)))
        return len(islands)

    def floodfill(self, r, c, shape, start, grid, visited):
        
        for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
            row, col = r+dx, c+dy
            if  (0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited and grid[row][col] == 1):
                visited.add((row, col))
                shape.append((row-start[0], col-start[1]))
                self.floodfill(row, col, shape, start, grid, visited)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends