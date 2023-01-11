class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = []
        pq = [(0, grid[start[0]][start[1]], start[0], start[1])]
        visited = set()
        visited.add((start[0], start[1]))
        
        while pq and k > 0:
            dist, price, r, c = heapq.heappop(pq)
            
            if pricing[0] <= price <= pricing[1]:
                ans.append([r, c])
                k -= 1
                
            for row, col in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
                if 0 <= row < n and 0 <= col < m and (row, col) not in visited and grid[row][col]:
                    visited.add((row, col))
                    heapq.heappush(pq, (dist+1, grid[row][col], row, col))
        return ans
                