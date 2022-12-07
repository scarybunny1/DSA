class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        matrix = [[-1] * n for _ in range(m)]
        k = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = original[k]
                k += 1
        return matrix