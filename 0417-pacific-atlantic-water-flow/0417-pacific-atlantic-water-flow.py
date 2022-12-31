class Solution:
    def waterFlow(self, q, visited, heights):
        n, m = len(heights), len(heights[0])
        while q:
            height, r, c = q.popleft()
            
            for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                row, col = r+dr, c+dc
                
                if 0 <= row < n and 0 <= col < m and (row, col) not in visited and heights[row][col] >= heights[r][c]:
                    visited.add((row, col))
                    q.append((heights[row][col], row, col))
                    
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        visited_pacific, visited_atlantic = set(), set()
        q_pacific, q_atlantic = deque(), deque()
        
        for i in range(n):
            q_pacific.append((heights[i][0], i, 0))
            visited_pacific.add((i, 0))
            
            q_atlantic.append((heights[i][m-1], i, m-1))
            visited_atlantic.add((i, m-1))
            
        for j in range(m):
            q_pacific.append((heights[0][j], 0, j))
            visited_pacific.add((0, j))
            
            q_atlantic.append((heights[n-1][j], n-1, j))
            visited_atlantic.add((n-1, j))
            
        self.waterFlow(q_pacific, visited_pacific, heights)
        self.waterFlow(q_atlantic, visited_atlantic, heights)
        
        ans = []
        for (row, col) in list(visited_pacific):
            if (row, col) in visited_atlantic:
                ans.append([row, col])
        return ans