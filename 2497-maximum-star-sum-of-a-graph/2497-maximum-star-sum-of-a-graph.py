class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        maxi = -inf
        q = collections.deque()
        visited = set()
        for i in range(len(vals)):
            if i in visited:
                continue
            visited.add(i)
            q.append(i)
            while q:
                node = q.popleft()
                pq = []
                for nei in graph[node]:
                    heapq.heappush(pq, vals[nei])
                    if len(pq) > k:
                        heapq.heappop(pq)
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                start_sum = vals[node]
                print(start_sum, pq)
                for val in pq:
                    start_sum = max(start_sum, start_sum+val)
                maxi = max(maxi, start_sum)
        return maxi