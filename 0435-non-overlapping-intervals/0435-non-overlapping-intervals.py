class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        intervals.sort(key= lambda x: x[1])
        skip = 0
        for start, end in intervals:
            if stack and start < stack[-1][1]:
                skip += 1
            else:
                stack.append([start, end])
        return skip