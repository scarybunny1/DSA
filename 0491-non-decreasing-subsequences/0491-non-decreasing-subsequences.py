class Solution:
    def increasingSubsequence(self, i, arr, nums, res):
        if i == len(nums):
            if len(arr) >= 2:
                res.add(tuple(arr))
            return
        
        if not arr or arr[-1] <= nums[i]:
            arr.append(nums[i])
            self.increasingSubsequence(i+1, arr, nums, res)
            arr.pop()
            
        self.increasingSubsequence(i+1, arr, nums, res)
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.increasingSubsequence(0, [], nums, res)
        return list(res)