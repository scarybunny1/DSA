class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
            
        stack = [source]
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return False