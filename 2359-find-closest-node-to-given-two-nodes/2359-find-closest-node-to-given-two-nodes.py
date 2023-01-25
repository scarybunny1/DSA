class Solution:
    def getDist(self, start, edges, dist):
        q = collections.deque([start])
        d = 1
        while q:
            node = q.popleft()
            neighbor = edges[node]
            if neighbor != -1 and dist[neighbor] == inf:
                dist[neighbor] = d
                q.append(neighbor)
            d += 1
        
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist1 = [inf]*len(edges)
        dist2 = [inf]*len(edges)
        dist1[node1] = 0
        dist2[node2] = 0
        self.getDist(node1, edges, dist1)
        self.getDist(node2, edges, dist2)
        
        closest = -1
        min_distance = inf
        for i in range(len(edges)):
            d = max(dist1[i], dist2[i])
            if d < min_distance:
                min_distance = d
                closest = i
        return closest
    
    
    
    # n1=2->5->4->3
    # n2=0->3