class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)        
        
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        NOTSET, BLUE, GREEN = -1, 0, 1
        color = BLUE
        colors = [NOTSET] * (n+1)
        q = collections.deque()
        visited = set()
        
        for person in range(1, n+1):
            if person not in visited:
                q.append((person, BLUE))
                visited.add(person)
                
                while q:
                    p, color = q.popleft()
                    
                    colors[p] = color
                    
                    for next_p in graph[p]:
                        if colors[next_p] == color:
                            return False
                        if next_p not in visited:
                            q.append((next_p, color ^ 1))
                            visited.add(next_p)
        return True
                            
            