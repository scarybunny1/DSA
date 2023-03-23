#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		res = []
		self.getSumOfSubsets(0, arr, 0, res)
		return res

    def getSumOfSubsets(self, i, arr, sum, res):
        if i == len(arr):
            res.append(sum)
            return
        
        self.getSumOfSubsets(i+1, arr, sum, res)
        self.getSumOfSubsets(i+1, arr, sum+arr[i], res)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends