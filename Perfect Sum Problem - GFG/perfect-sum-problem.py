#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
	    memo = [[-1]*(sum+1) for _ in range(n)]
		return self.sumCount(0, arr, n, sum, memo)

    def sumCount(self, i, nums, n, target, memo):
        if i == n:
            if target == 0:
                return 1
            return 0
        if memo[i][target] == -1:
            MOD = 10**9+7
            take = 0
            not_take = self.sumCount(i+1, nums, n, target, memo)
            if nums[i] <= target:
                take = self.sumCount(i+1, nums, n, target-nums[i], memo)
            memo[i][target] = (take + not_take) % MOD
        return memo[i][target]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends