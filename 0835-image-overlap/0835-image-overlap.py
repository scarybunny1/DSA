class Solution:
    def getNonZeroCells(self, matrix, n):
        res = []
        for x in range(n):
            for y in range(n):
                if matrix[x][y] == 1:
                    res.append((x, y))
        return res
    
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        non_zero_img1 = self.getNonZeroCells(img1, n)
        non_zero_img2 = self.getNonZeroCells(img2, n)
        
        max_overlap = 0
        transformations = defaultdict(int)
        
        for row1, col1 in non_zero_img1:
            for row2, col2 in non_zero_img2:
                vec = (row2-row1, col2-col1)
                transformations[vec] += 1
                
                max_overlap = max(max_overlap, transformations[vec])
        
        return max_overlap