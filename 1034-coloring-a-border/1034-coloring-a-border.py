class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        q = collections.deque([(row, col)])
        initial_color = grid[row][col]
        visited = set([(row, col)])
        while q:
            r, c = q.popleft()
            for row, col in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                if (row, col) in visited:
                    continue
                if not (0 <= row < n and 0 <= col < m) or grid[row][col] != initial_color:
                    grid[r][c] = color
                    continue
                visited.add((row, col))
                q.append((row, col))
        return grid