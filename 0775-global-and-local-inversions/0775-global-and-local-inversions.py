class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # """Explanation: All local inversions are global inversions. For both to be equal there must not be any global inversions other than local ones. If other can be formed, return False. Other definition: When nums[i] is not at i-1, i, i+1"""
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True