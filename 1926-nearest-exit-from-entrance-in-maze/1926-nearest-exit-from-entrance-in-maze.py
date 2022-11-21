class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        q = collections.deque([entrance])
        
        steps = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                    row, col = r+dr, c+dc
                    if not (0 <= row < n and 0 <= col < m):
                        if [r, c] != entrance:
                            return steps
                    elif maze[row][col] == '.' and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
            steps += 1
        return -1