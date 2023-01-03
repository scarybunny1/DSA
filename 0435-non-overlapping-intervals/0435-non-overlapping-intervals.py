class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        
        stack = []
        overlap = 0
        
        for interval in intervals:
            if stack and stack[-1][1] > interval[0]:
                overlap += 1
            else:
                stack.append(interval)
        return overlap