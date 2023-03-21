#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        res = []
        self.generate(0, n, '', res)
        return res
        
    def generate(self, i, n, string, res):
        if i == n:
            res.append(string)
            return
        self.generate(i+1, n, string+'0', res)
        if not string or string[-1] != '1':
            self.generate(i+1, n, string+'1', res)
        

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
# } Driver Code Ends