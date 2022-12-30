class Solution:
    def isPossible(self, limit, splits, nums):
        curr_sum = 0
        s = 1
        for num in nums:
            if num > limit:
                return False
            if num + curr_sum > limit:
                s += 1
                curr_sum = num
            else:
                curr_sum += num
        if curr_sum > limit:
            return False
        return s <= splits
            
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            
            if self.isPossible(mid, k, nums):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans