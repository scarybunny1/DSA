class Solution:
    def doesOverlap(self, interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        
        if end - start >= 0:
            return [start, end]
        return []
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = second = 0
        res = []
        
        while first < len(firstList) and second < len(secondList):
            overlap = self.doesOverlap(firstList[first], secondList[second])
            
            if overlap:
                res.append(overlap)
                
            if firstList[first][1] > secondList[second][1]:
                second += 1
            elif secondList[second][1] > firstList[first][1]:
                first += 1
            else:
                first =+ 1
                second += 1
        
        return res