class Solution:
    def findCycle(self, node, graph, path, visited):
        path.add(node)
        visited.add(node)
        for nei in graph[node]:
            if nei in path:
                return True
            if nei not in visited:
                if self.findCycle(nei, graph, path, visited):
                    return True
        path.remove(node)
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """BFS"""
#         n = len(graph)
#         revGraph = defaultdict(list)
#         indegree = [0]*n
#         for node, neighborList in enumerate(graph):
#             for neighbor in neighborList:
#                 indegree[node] += 1
#                 revGraph[neighbor].append(node)
#         q = deque()
#         for node in range(n):
#             if indegree[node] == 0:
#                 q.append(node)
#         safe = [0]*n
#         while q:
#             node = q.popleft()
#             safe[node] = 1
#             for nei in revGraph[node]:
#                 indegree[nei] -= 1
#                 if indegree[nei] == 0:
#                     q.append(nei)
#         return [x for x in range(n) if safe[x] == 1]
        
#         """DFS"""
#         visited = set()
#         path = set()
#         n = len(graph)
#         res = []
#         for node in range(n):
#             if node not in visited:
#                 self.findCycle(node, graph, path, visited)
#         for i in range(n):
#             if i not in path:
#                 res.append(i)
#         return res
    
    
        """Doing it again"""
        path = set()
        visited = set()
        
        res = []
        
        for i in range(len(graph)):
            if i not in visited:
                visited.add(i)
                self.checkCycle(i, visited, path, graph)
        for i in range(len(graph)):
            if i not in path:
                res.append(i)
        return res
    
    
    
    
    def checkCycle(self, node, visited, path, graph):
        
        path.add(node)
        for nei in graph[node]:
            if nei in path:
                return True
            if nei not in visited:
                visited.add(nei)
                if self.checkCycle(nei, visited, path, graph):
                    return True
        path.remove(node)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    