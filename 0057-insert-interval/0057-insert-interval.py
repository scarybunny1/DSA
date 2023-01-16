class Solution:
    def insertPos(self, interval, intervals):
        left, right = 0, len(intervals)-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            
            if interval[0] < intervals[mid][0]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return len(intervals) if ans == -1 else ans
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = self.insertPos(newInterval, intervals)
        
        intervals = intervals[:pos] + [newInterval] + intervals[pos:]
        
        stack = []
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                temp = stack.pop()
                stack.append([temp[0], max(temp[1], end)])
            else:
                stack.append([start, end])
        return stack