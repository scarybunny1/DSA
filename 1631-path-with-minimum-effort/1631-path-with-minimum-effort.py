class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        efforts = [[float('inf')]*m for _ in range(n)]
        efforts[0][0] = 0
        while heap:
            effort, row, col = heapq.heappop(heap)
                
            if [row, col] == [n-1, m-1]:
                return effort

            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                r, c = row+dx, col+dy
                if (0 <= r < n and 0 <= c < m):
                    
                    new_effort = max(effort, abs(heights[r][c] - heights[row][col]))
                    if new_effort < efforts[r][c]:
                        heapq.heappush(heap, (new_effort, r, c))
                        efforts[r][c] = new_effort
        return efforts[n-1][m-1]