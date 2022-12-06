class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #1. For each number in range [1, n], iterate over the array to check if it is present. TC: O(n^2)
        
        #2. Use a set to check if the number from range [1, n] is present in the nums array TC: O(n) SC: O(n)

        #3. Change the sign of the numbers seen. Using the fact that the number's value lie in the range [1, n]
        
        # 4 3 2 7 8 2 3 1
        # 0 1 2 3 4 5 6 7
        
        for num in nums:
            val = abs(num)
            nums[val-1] = -abs(nums[val-1])
            
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res