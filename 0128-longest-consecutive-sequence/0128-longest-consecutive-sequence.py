class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for num in nums:
            if num-1 in s:
                continue
            curr = 1
            n = num+1
            while n in s:
                curr += 1
                n += 1
            longest = max(longest, curr)
        
        return longest
        
#         set = {100, 4, 200, 1, 3, 2}
#         100, 4, 200, 1, 3, 2
        
#         100 check if num+1 in set
#         also check if 100 is not part of another sequence, if 100-1 in set
        
#         100, 101 not in set, longest = 1
#         4, 5 not in set, longest = 1
#         200, 201 not in set, longest = 1
#         1, 2 in set, 3 in set, 4 in set, longest = 4
        
        
#         1,2,3,4,5
#         1, longest = 5
#         2, if 2-1 in set, continue