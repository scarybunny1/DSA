class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        queries = [(i, q) for i, q in enumerate(queries)]
        queries.sort(key= lambda x: x[1])
        ans = [0]*len(queries)
        count = 0
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        for i, q in queries:
            while pq and pq[0][0] < q:
                val, r, c = heapq.heappop(pq)
                count += 1
                for row, col in [r+1, c], [r, c+1], [r-1, c], [r, c-1]:
                    if 0 <= row < n and 0 <= col < m and (row, col) not in visited:
                        heapq.heappush(pq, (grid[row][col], row, col))
                        visited.add((row, col))
            ans[i] = count
        return ans