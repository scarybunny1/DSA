class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_capture = 0
        start = None
        fort = None
        for i in range(len(forts)):
            if forts[i] == 1 or forts[i] == -1:
                if fort and forts[i] == -fort:
                    max_capture = max(max_capture, i - start - 1)
                fort = forts[i]
                start = i
        return max_capture