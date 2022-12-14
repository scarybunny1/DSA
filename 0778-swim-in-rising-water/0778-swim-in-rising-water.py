class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minimum_time_required = 0
        heap = [[grid[0][0], 0, 0]]
        visited = set([(0, 0)])
        
        while True:
            time, r, c = heapq.heappop(heap)
            minimum_time_required = max(time, minimum_time_required)
            
            if (r, c) == (n-1, n-1):
                return minimum_time_required
            
            for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                row, col = r+dr, c+dc
                
                if 0 <= row < n and 0 <= col < n and (row, col) not in visited:
                    visited.add((row, col))
                    heapq.heappush(heap, [grid[row][col], row, col])
        