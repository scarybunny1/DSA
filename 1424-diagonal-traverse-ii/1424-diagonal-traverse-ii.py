class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        heap = []
        n, m = len(mat), len(mat[0])
        for i in range(n):
            j = 0
            while j < len(mat[i]):
                heapq.heappush(heap, (i+j, j, i))
                j += 1
        
        res = []
        while heap:
            _, j, i = heapq.heappop(heap)
            res.append(mat[i][j])
        return res