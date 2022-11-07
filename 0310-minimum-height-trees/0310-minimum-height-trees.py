class Solution:
    def dfs(self, node, parent, height, d, depth, graph):
        
        depth[node] = d
        h = -1
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            h = max(h, self.dfs(neighbor, node, height, d+1, depth, graph))
        height[node] = h + 1
        
        return h+1
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        # height = defaultdict(int)
        # depth = defaultdict(int)
        
        for node, neighbor in edges:
            graph[node].add(neighbor)
            graph[neighbor].add(node)
#         print(graph)
#         self.dfs(0, -1, height, 0, depth, graph)
#         print(height.items(), depth.items())
#         mht = [max(height[i],depth[i]) for i in range(n)]
#         print(height.items(), depth.items(), mht)
        
#         minimum_mht = min(mht)
        
#         return [i for i in range(n) if mht[i] == minimum_mht]
        leaves = [i for i in range(n) if len(graph[i]) <= 1]
    
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
            
            
            
            
            
            
            