class Solution:
    def splitOperationsRequired(self, nums, maxSize):
        operations = 0
        for num in nums:
            operations += (num-1) // maxSize
        return operations
        
        
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            
            operations = self.splitOperationsRequired(nums, mid)
            if operations <= maxOperations:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans