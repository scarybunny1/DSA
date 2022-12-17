class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            diff = set()
            for j in range(len(arr)-1):
                diff.add(arr[j+1]-arr[j])
            if len(diff) > 1:
                res.append(False)
            else:
                res.append(True)
        return res