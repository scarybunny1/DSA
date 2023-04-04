from typing import List
import collections
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		q = collections.deque()
        visited = set()
        for i in range(V):
            if i in visited:
                continue
            visited.add(i)
            q.append((i, -1))
            while q:
                node, parent = q.popleft()
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return 1
                    visited.add(nei)
                    q.append((nei, node))
        return 0
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends