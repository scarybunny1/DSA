#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        visited = set()
        
        mst = []
        mst_sum = 0
        
        heap = [(0, 0, -1)]
        
        while heap:
            weight, node, parent = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            mst_sum += weight
            if parent != -1:
                mst.append((node, parent))
                
            for neighbor, edge_weight in adj[node]:
                heapq.heappush(heap, (edge_weight, neighbor, node))

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