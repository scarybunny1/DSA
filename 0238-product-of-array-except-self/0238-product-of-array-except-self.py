class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        product = 1
        for i in range(n-1):
            product *= nums[i]
            ans[i+1] = product
            
        product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= product
            product *= nums[i]
            
        return ans