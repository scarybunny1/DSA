class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # O(n) solution
        # res = []
        # nums.sort()
        # for total in queries:
        #     left = 0
        #     max_len = 0
        #     curr_sum = 0
        #     for right in range(len(nums)):
        #         curr_sum += nums[right]
        #         while curr_sum > total:
        #             curr_sum -= nums[left]
        #             left += 1
        #         max_len = max(max_len, right - left + 1)
        #     res.append(max_len)
        # return res
    
        #O(logn) solution using Binary search
        res = []
        nums.sort()
        arr = list(accumulate(nums))
        for total in queries:
            ans = self.search(arr, total)
            res.append(ans + 1)
        return res
    
    def search(self, nums, total):
        left, right = 0, len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= total:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans