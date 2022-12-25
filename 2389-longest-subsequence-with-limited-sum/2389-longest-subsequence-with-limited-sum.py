class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        for total in queries:
            left = 0
            max_len = 0
            curr_sum = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                while curr_sum > total:
                    curr_sum -= nums[left]
                    left += 1
                max_len = max(max_len, right - left + 1)
            res.append(max_len)
        return res