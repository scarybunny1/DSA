#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        distance = [100000000] * V
        distance[S] = 0
        for _ in range(V-1):
            for node, neighbor, edge_weight in edges:
                if distance[node] + edge_weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + edge_weight
                    
        for node, neighbor, edge_weight in edges:
            if distance[node] + edge_weight < distance[neighbor]:
                return [-1]
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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends