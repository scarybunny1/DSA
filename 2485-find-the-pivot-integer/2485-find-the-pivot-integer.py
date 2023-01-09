class Solution:
    def pivotInteger(self, n: int) -> int:
        # 1 2 3 4 5 6 7 8
        #   i
        left, right = 0, sum(x for x in range(1,n+1))
        for i in range(1, n+1):
            left += i
            if left == right:
                return i
            right -= i
        return -1