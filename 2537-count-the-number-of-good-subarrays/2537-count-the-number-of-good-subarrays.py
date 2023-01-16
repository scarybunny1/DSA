class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs = 0
        d = defaultdict(int)
        n = len(nums)
        left = right = 0
        ans = 0
        while right < n:
            d[nums[right]] += 1
            pairs += d[nums[right]] - 1
            while pairs >= k:
                ans += n - right
                d[nums[left]] -= 1
                pairs -= d[nums[left]]
                left += 1
            right += 1
        return ans