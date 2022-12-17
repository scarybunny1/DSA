class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxi = 0
        prod = 1
        left = 0
        for right in range(len(nums)):
            prod *= nums[right]
            if prod > 0:
                maxi = max(maxi, right - left + 1)
            elif prod == 0:
                prod = 1
                left = right + 1
        right2 = len(nums)-1
        prod = 1
        for left2 in range(len(nums)-1, -1, -1):
            prod *= nums[left2]
            if prod > 0:
                maxi = max(maxi, right2 - left2 + 1)
            elif prod == 0:
                prod = 1
                right2 = left2 - 1
        return maxi