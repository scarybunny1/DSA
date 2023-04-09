#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, graph):
        #code here
        mst_sum = 0
        visited = set()
        
        pq = [(0, 0)]
        while pq:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            mst_sum += weight
            for nei, w in graph[node]:
                heapq.heappush(pq, (w, nei))
        return mst_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends