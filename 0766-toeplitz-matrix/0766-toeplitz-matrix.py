class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i-j in d and matrix[i][j] != d[i-j]:
                    return False
                elif i-j not in d:
                    d[i-j] = matrix[i][j]
        return True