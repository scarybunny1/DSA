class Solution:
    def insert_pos(self, intervals, newInterval):
        left, right = 0, len(intervals)
        ans = -1
        while left < right:
            mid = (left + right) // 2
            if newInterval[0] > intervals[mid][0]:
                left = mid + 1
            else:
                right = mid
        return left
            
            
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort()
        insertPos = self.insert_pos(intervals, newInterval)
        intervals = intervals[:insertPos] + [newInterval] + intervals[insertPos:]
        stack = []
        for start, end in intervals:
            if stack and (stack[-1][0]<=start<=stack[-1][1] or stack[-1][0]<=end<=stack[-1][1]):
                new_interval = stack.pop()
                stack.append([min(new_interval[0], start), max(new_interval[1], end)])
            else:
                stack.append([start, end])
        return stack
        