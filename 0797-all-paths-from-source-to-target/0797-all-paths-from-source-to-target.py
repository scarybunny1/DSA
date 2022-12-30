class Solution:
    def getPath(self, node, arr, graph, destination, res):
        if node == destination:
            res.append(list(arr))
            return
        
        for neighbor in graph[node]:
            arr.append(neighbor)
            self.getPath(neighbor, arr, graph, destination, res)
            arr.pop()
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        self.getPath(0, [0], graph, n-1, res)
        return res