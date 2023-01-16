class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        pairs = ans = 0
        d = defaultdict(int)
        for right in range(n):
            d[nums[right]] += 1
            pairs += d[nums[right]] - 1
            
            while pairs >= k:
                ans += n - right
                d[nums[left]] -= 1
                pairs -= d[nums[left]]
                left += 1
        return ans