class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        inc = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if inc == 0:
                    inc = 1
                elif inc == -1:
                    return False
            elif nums[i] < nums[i-1]:
                if inc == 0:
                    inc = -1
                elif inc == 1:
                    return False
        return True