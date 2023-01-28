class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.nums = []

    def addNum(self, value: int) -> None:
        bisect.insort(self.nums, value)
        
        intervals = []
        left = right = 0
        for i in range(1, len(self.nums)):
            if self.nums[i] - self.nums[right] <= 1:
                right = i
            else:
                intervals.append([self.nums[left], self.nums[right]])
                left = right = i
        intervals.append([self.nums[left], self.nums[right]])
        self.intervals = intervals

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
