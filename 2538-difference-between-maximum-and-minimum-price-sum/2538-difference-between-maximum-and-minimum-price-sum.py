class Solution:
    def getMaxPathSum(self, node, parent, graph, price, memo):
        if (node, parent) in memo:
            return memo[(node, parent)]
        
        max_sum = 0
        for nei in graph[node]:
            if nei == parent:
                continue
            max_sum = max(max_sum, self.getMaxPathSum(nei, node, graph, price, memo))
        
        max_sum += price[node]
        memo[(node, parent)] = max_sum
        return max_sum
        
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        max_cost = 0
        memo = {}
        for node in range(n):
            max_price = self.getMaxPathSum(node, -1, graph, price, memo)
            min_price = price[node]
            max_cost = max(max_cost, max_price - min_price)
        return max_cost