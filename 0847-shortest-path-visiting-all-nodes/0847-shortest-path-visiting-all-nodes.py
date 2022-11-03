class Solution:

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        path = 0
        visited = set()
        q = collections.deque()
        n = len(graph)
        desired_bitmask = (1 << n) - 1
        
        for i in range(n):
            bm = 1 << i
            q.append((i, bm))
            visited.add((i, bm))
            
        while q:
            for _ in range(len(q)):
                node, bitmask = q.popleft()
                if bitmask == desired_bitmask:
                    return path
                
                for nei in graph[node]:
                    new_bitmask = bitmask | (1 << nei)
                    if (nei, new_bitmask) not in visited:
                        visited.add((nei, new_bitmask))
                        q.append((nei, new_bitmask))
            path += 1
            
        return -1
    
    
    