class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # 6:53:30
        
        # i+1 th rotation = ith rotation + N * A[i] - sum(A)
        n = len(nums)
        total = sum(nums)
        last_rotation = sum(i*nums[i] for i in range(n))
        maxi = last_rotation
        for i in range(1, n):
            next_rotation = last_rotation + n * nums[i-1] - total
            maxi = max(maxi, next_rotation)
            last_rotation = next_rotation
            
        return maxi