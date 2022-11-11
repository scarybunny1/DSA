class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                nums[j] = 101
                j += 1
            i = j
        
        left = right = 0
        while right < n:
            while right < n and nums[right] == 101:
                right += 1
            if right == n:
                break
            nums[left] = nums[right]
            left += 1
            right += 1
        return left
    
    # 0 101 1 101 101 2 101 3 101 4
    #    l
    #       r