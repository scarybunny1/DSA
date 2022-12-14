class Solution:
    def robHouse(self, houseNo, nums, memo):
        if houseNo < 0:
            return 0
        if houseNo == 0:
            return nums[houseNo]
        if houseNo in memo:
            return memo[houseNo]
        
        rob = nums[houseNo] + self.robHouse(houseNo-2, nums, memo)
        leave = self.robHouse(houseNo-1, nums, memo)
        
        memo[houseNo] = max(rob, leave)
        
        return memo[houseNo]
    
    def rob(self, nums: List[int]) -> int:
        """Recursive Approach"""
        memo = {}
        return self.robHouse(len(nums)-1, nums, memo)

        """Iterative Approach"""
        n = len(nums)
        lastHouse = lastLastHouse = 0
        for i in range(n):
            lastHouse, lastLastHouse = max(lastHouse, lastLastHouse + nums[i]), lastHouse
        return lastHouse
    
    