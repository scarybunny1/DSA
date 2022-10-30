class Solution:
    def isSafe(self, row, col, n, m):
        return (0 <= row < n) and (0 <= col < m)
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([(0, 0, 0, k)])
        n, m = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while q:
            row, col, steps, obs = q.popleft()
            
            if (row, col) == (n-1, m-1):
                return steps
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if self.isSafe(new_row, new_col, n, m):
                    if grid[new_row][new_col] == 1 and obs > 0 and (new_row, new_col, obs-1) not in visited:
                        q.append((new_row, new_col, steps + 1, obs - 1))
                        visited.add((new_row, new_col, obs-1))
                    elif grid[new_row][new_col] == 0 and (new_row, new_col, obs) not in visited:
                        q.append((new_row, new_col, steps + 1, obs))
                        visited.add((new_row, new_col, obs))
        return -1