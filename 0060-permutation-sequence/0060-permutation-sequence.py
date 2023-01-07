class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        arr = [i for i in range(1, n+1)]
        N = n
        k-=1
        for _ in range(n):
            index = k // factorial(N-1)
            ans.append(arr[index])
            arr.pop(index)
            k -= (index+1)*factorial(N-1)
            N -= 1
        return "".join(map(str, ans))