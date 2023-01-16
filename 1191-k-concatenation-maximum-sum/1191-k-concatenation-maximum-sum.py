class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        #Input: arr and integer k, representng arr is repeated k times
        #Output: max subarray sum
        
        #Brute Force: Repeat arr k times and apply kadane's on it.
        #TC is O(n*k)
        
        #Better Solution: Simplify into cases
        
        #If k == 1, simply apply kadane's algorithm
        if k == 1:
            nums = arr
        #If k > 1, we need to use the arr more than once, apply kadane's for arr repeated twice
        else:
            nums = arr + arr
        max_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        #Check if sum(arr) > 0 or not. 
        #If it is, max_subarray_sum will include all intermediate repetitions of arr
        if sum(arr) > 0 and k > 2:
            max_sum += sum(arr) * (k - 2)
            
        return max_sum % (10**9+7)
        