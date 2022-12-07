class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        hare = tortoise = nums[0]
        
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break
                
        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        
        return hare