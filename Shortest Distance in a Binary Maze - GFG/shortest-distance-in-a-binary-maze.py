#User function Template for python3

from typing import List
import collections
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        # path = 0
        # visited = set([(source[0], source[1])])
        # q = collections.deque([(source[0], source[1])])
        # while q:
        #     for _ in range(len(q)):
        #         row, col = q.popleft()
        #         if [row, col] == destination:
        #             return path
                
        #         for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
        #             r, c = row+dx, col+dy
        #             if (0 <= r < n and 0 <= c < m and (r, c) not in visited and grid[r][c]):
        #                 visited.add((r, c))
        #                 q.append((r, c))
        #     path += 1
        # return -1
        
        q = collections.deque([(source[0], source[1])])
        distance = [[float('inf')] * m for _ in range(n)]
        distance[source[0]][source[1]] = 0
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if [row, col] == destination:
                    return distance[row][col]
                for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    r, c = row+dx, col+dy
                    if 0 <= r < n and 0 <= c < m and grid[r][c] and 1 + distance[row][col] < distance[r][c]:
                        distance[r][c] = 1 + distance[row][col]
                        q.append((r, c))
        return -1
                
                
                
                
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends