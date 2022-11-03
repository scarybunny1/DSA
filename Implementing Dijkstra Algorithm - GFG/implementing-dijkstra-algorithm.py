import heapq
import math

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        distance = [math.inf] * V
        distance[S] = 0
        heap = [(0, S)]
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            for neighbor_node, edge_weight in adj[node]:
                if dist + edge_weight < distance[neighbor_node]:
                    distance[neighbor_node] = dist + edge_weight
                    heapq.heappush(heap, (dist + edge_weight, neighbor_node))
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends