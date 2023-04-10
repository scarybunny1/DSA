#User function Template for python3
import collections
import math
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        dist = [math.inf] * n
        dist[src] = 0
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = collections.deque()
        q.append(src)
        distance = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    if dist[nei] > distance:
                        dist[nei] = distance
                        q.append(nei)
            distance += 1
        for i in range(n):
            if dist[i] == math.inf:
                dist[i] = -1
        return dist
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends