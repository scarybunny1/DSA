class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #Use XOR operation, first occurence will add info to the ans and second occurence will nullify that info. Eventually, ans will contain the only single element appearing once.
        #TC: O(n) SC: O(1)
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
    
        #Add in set for first occurence and delete for second. Only element remaining will be the single element
        #TC: O(n) SC: O(n)
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()