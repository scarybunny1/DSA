class Solution:
    def findParent(self, node, root):
        if node == root[node]:
            return node
        root[node] = self.findParent(root[node], root)
        return root[node]
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # DFS
#         e = len(connections)
#         if e < n-1:
#             return -1
#         graph = defaultdict(list)
#         for u, v in connections:
#             graph[u].append(v)
#             graph[v].append(u)
#         visited = set()
        
#         def dfs(node):
#             if node in visited:
#                 return 0
#             visited.add(node)
#             for nei in graph[node]:
#                 dfs(nei)
#             return 1
        
#         return sum(dfs(x) for x in range(n))-1
        if len(connections) < n - 1:
            return -1
        root = [i for i in range(n)]
        for node, neighbor in connections:
            rootNode = self.findParent(node, root)
            rootNeighbor = self.findParent(neighbor, root)
            if rootNode != rootNeighbor:
                root[rootNeighbor] = rootNode
        return sum(1 for i, node in enumerate(root) if i == node) - 1