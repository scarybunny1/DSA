class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
#         [1,4,3,1,3,2],
#         [3,2,1,3,2,4],
#         [2,3,3,2,3,1]
        
        
#         [3,3,3,3,3],
#         [3,2,2,2,3],
#         [3,2,1,2,3],
#         [3,2,2,2,3],
#         [3,3,3,3,3]
        n, m = len(heightMap), len(heightMap[0])
        visited = set()
        pq = []
        
        for j in range(m):
            pq.append((heightMap[0][j], 0, j))
            pq.append((heightMap[n-1][j], n-1, j))
            visited.add((0, j))
            visited.add((n-1, j))
            
        for i in range(1, n-1):
            pq.append((heightMap[i][0], i, 0))
            pq.append((heightMap[i][m-1], i, m-1))
            visited.add((i, 0))
            visited.add((i, m-1))
            
        heapq.heapify(pq)
        level = 0
        water = 0
        while pq:
            height, x, y = heapq.heappop(pq)
            level = max(height, level)
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                row, col = x+dx, y+dy
                
                if 0 <= row < n and 0 <= col < m and (row, col) not in visited:
                    if heightMap[row][col] < level:
                        water += level - heightMap[row][col]
                    visited.add((row, col))
                    heapq.heappush(pq, (heightMap[row][col], row, col))
        return water