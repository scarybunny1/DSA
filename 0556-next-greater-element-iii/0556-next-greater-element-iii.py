class Solution:
    def justGreaterThan(self, num, left, right, arr):
        ans = left
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] > num:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
    def nextGreaterElement(self, n: int) -> int:
        # [2,4,6,2,3,2,1,0]
        
        arr = list(str(n))
        right = -1
        for j in range(len(arr)-2, -1, -1):
            if arr[j] < arr[j+1]:
                right = j
                break
        if right == -1:
            return -1
        
        next_greater = self.justGreaterThan(arr[right], right+1, len(arr)-1, arr)
        arr[right], arr[next_greater] = arr[next_greater], arr[right]
        
        s = "".join(arr[:right+1] + arr[right+1:][::-1])
        num = int(s)
        return -1 if num > 2**31-1 else num