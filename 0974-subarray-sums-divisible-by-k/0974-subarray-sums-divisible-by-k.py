class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 4 5 0 -2 -3 1 k=5
        # 4 9 9  7  4 5
        #             i
        # d = {0:2, 4:4, 2:1}
        # ans = 1+2+3+1
        
        d = {0:1}
        ans = 0
        for num in accumulate(nums):
            rem = ((num % k) + k) % k
            if rem in d:
                ans += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
        return ans