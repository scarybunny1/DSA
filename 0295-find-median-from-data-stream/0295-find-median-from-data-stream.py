class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min, num)
        heapq.heappush(self.max, -heapq.heappop(self.min))
        if len(self.max) > len(self.min) + 1:
            heapq.heappush(self.min, -heapq.heappop(self.max))

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        if len(self.max) == len(self.min):
            return (self.min[0] - self.max[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()