class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans = set()
        n = len(nums)
        for i in range(n):
            count = 0
            key = ""
            for j in range(i, n):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                key += f"{nums[j]}-"
                ans.add(key)
        return len(ans)