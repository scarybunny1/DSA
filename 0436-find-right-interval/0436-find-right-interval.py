class Solution:
    def findRight(self, target, nums):
        left, right = 0, len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = [(start, end, i) for i, (start, end) in enumerate(intervals)]
        nums.sort()
        
        ans = []
        for start, end in intervals:
            index = self.findRight(end, nums)
            ans.append(nums[index][2] if index != -1 else -1)
        return ans