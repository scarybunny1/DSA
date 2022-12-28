class Solution:
    def calculate(self, source, destination, graph):
        visited = set([source])
        q = collections.deque([(source, 1)])
        
        while q:
            node, weight = q.popleft()
            if node == destination:
                return weight
            
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, weight*w))
        return -1.0
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for weight, (node, neighbor) in zip(values, equations):
            graph[node].append((neighbor, weight))
            graph[neighbor].append((node, 1 / weight))
            
        ans = []
        for x, y in queries:
            if x in graph and y in graph:
                ans.append(self.calculate(x, y, graph))
            else:
                ans.append(-1)
        return ans