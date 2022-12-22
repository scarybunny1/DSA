class Solution:
    def calculateSubtreeSum(self, node, parent, count, ans, graph):
        for child in graph[node]:
            if child != parent:
                self.calculateSubtreeSum(child, node, count, ans, graph)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
    
    def findAns(self, node, parent, count, ans, graph, n):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + (n - count[child])
                self.findAns(child, node, count, ans, graph, n)
        
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [1] * n
        ans = [0] * n
        
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        self.calculateSubtreeSum(0, -1, count, ans, graph)
        self.findAns(0, -1, count, ans, graph, n)
        return ans