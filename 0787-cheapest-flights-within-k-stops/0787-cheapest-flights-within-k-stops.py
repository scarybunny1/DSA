class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = defaultdict(list)
#         for start, end, price in flights:
#             graph[start].append((end, price))
            
#         heap = [(-1, src, 0)]
#         temp = [inf]*n
#         while heap:
#             print(heap)
#             stops, city, price = heapq.heappop(heap)
#             if city == dst:
#                 return price
#             if stops == k:
#                 continue
#             for neighbor, cost in graph[city]:
#                 if price + cost < temp[neighbor]:
#                     temp[neighbor] = price + cost
#                     heapq.heappush(heap, (stops + 1, neighbor, temp[neighbor]))
#         return -1
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
        q = collections.deque([(-1, src, 0)])
        ans = inf
        
        costs = [inf]*n
        
        while q:
            stops, city, cost = q.popleft()
            if city == dst:
                ans = min(ans, cost)
                continue
            if stops == k:
                continue

            for neighbor, price in graph[city]:
                if price + cost < costs[neighbor]:
                    costs[neighbor] = price + cost
                    q.append((stops + 1, neighbor, cost+price))
                
        return -1 if ans == inf else ans
