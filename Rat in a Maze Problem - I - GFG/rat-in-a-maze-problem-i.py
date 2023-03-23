#User function Template for python3

class Solution:
    def findPath(self, m, n):
        if m[n-1][n-1] == 0 or m[0][0] == 0:
            return []
        res = []
        self.dfs(0, 0, "", m, set(), n, res)
        return res

    def dfs(self, row, col, path, grid, visited, n, res):
        if (row, col) == (n-1, n-1):
            res.append(path)
            return
        
        if not (0 <= row < n) or not (0 <= col < n) or (row, col) in visited or grid[row][col] == 0:
            return
        
        visited.add((row, col))
        
        for dr, dc, char in [[1, 0, "D"], [0, -1, "L"], [0, 1, "R"], [-1, 0, "U"]]:
            self.dfs(row+dr, col+dc, path+char, grid, visited, n, res)

        visited.remove((row, col))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends