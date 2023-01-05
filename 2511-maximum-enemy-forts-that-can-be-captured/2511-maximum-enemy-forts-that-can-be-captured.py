class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_capture = 0
        start = -1
        enemy = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                start = i
                enemy = 0
            elif forts[i] == 0:
                if start != -1:
                    enemy += 1
            else:
                max_capture = max(max_capture, enemy)
                enemy = 0
                start = -1
        
        start = -1
        enemy = 0
        for i in range(len(forts)-1, -1, -1):
            if forts[i] == 1:
                start = i
                enemy = 0
            elif forts[i] == 0:
                if start != -1:
                    enemy += 1
            else:
                max_capture = max(max_capture, enemy)
                enemy = 0
                start = -1
        return max_capture