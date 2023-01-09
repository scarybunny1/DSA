class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y, w in roads:
            graph[x].append((y, w))
            graph[y].append((x, w))
            
        q = collections.deque([1])
        seen = set([1])
        min_score = inf
        while q:
            city = q.popleft()
            for neighbor, weight in graph[city]:
                min_score = min(min_score, weight)
                
                if neighbor in seen:
                    continue
                
                q.append(neighbor)
                seen.add(neighbor)
        return min_score