#User function Template for python3
import heapq
class Solution:
    def find(self, x, root):
        if x == root[x]:
            return x
        root[x] = self.find(root[x], root)
        return root[x]
    
    def union(self, x, y, root, rank):
        rootX = self.find(x, root)
        rootY = self.find(y, root)
        
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                root[rootX] = rootY
            else:
                root[rootY] = rootX
                rank[rootX] += 1
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # visited = set()
        
        # mst = []
        # mst_sum = 0
        
        # heap = [(0, 0, -1)]
        
        # while heap:
        #     weight, node, parent = heapq.heappop(heap)
        #     if node in visited:
        #         continue
        #     visited.add(node)
        #     mst_sum += weight
        #     if parent != -1:
        #         mst.append((node, parent))
                
        #     for neighbor, edge_weight in adj[node]:
        #         heapq.heappush(heap, (edge_weight, neighbor, node))

        # return mst_sum
        
        root = {i:i for i in range(V)}
        rank = [0]*V
        
        edges = []
        for node, neighbor_list in enumerate(adj):
            for neighbor, weight in neighbor_list:
                edges.append([weight, node, neighbor])
        edges.sort()
        
        mst_sum = 0
        mst = []
        for edge in edges:
            edge_weight, node, neighbor = edge[0], edge[1], edge[2]
            if self.find(node, root) != self.find(neighbor, root):
                self.union(node, neighbor, root, rank)
                mst.append(edge)
                mst_sum += edge_weight
        
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