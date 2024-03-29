class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = defaultdict(list)
#         for x, y, price in flights:
#             graph[x].append((y, price))
        
#         pq = [(0, -1, src)]
#         s = [inf]*n
        
#         while pq:
#             price, stops, city = heappop(pq)
            
#             if stops > k or stops >= s[city]:
#                 continue
#             if city == dst:
#                 return price
            
#             s[city] = stops
#             for neighbor, cost in graph[city]:
#                 heappush(pq, (price + cost, stops + 1, neighbor))
#         return -1
    
        graph = defaultdict(list)
        for x, y, price in flights:
            graph[x].append((y, price))
        
        q = collections.deque([(-1, 0, src)])
        costs = [inf] * n
        
        while q:
            stops, cost, city = q.popleft()
            if stops == k:
                continue
            for nei, price in graph[city]:
                if cost + price < costs[nei]:
                    costs[nei] = cost + price
                    q.append((stops+1, cost+price, nei))
        return -1 if costs[dst]==inf else costs[dst]