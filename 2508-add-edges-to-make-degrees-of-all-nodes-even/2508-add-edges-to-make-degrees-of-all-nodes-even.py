class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degree = [set() for _ in range(n+1)]
        
        for x, y in edges:
            degree[x].add(y)
            degree[y].add(x)
        
        odd_degree_nodes = []
        for node in range(1, n+1):
            if len(degree[node]) % 2 == 1:
                odd_degree_nodes.append(node)
        
        if len(odd_degree_nodes) == 0:
            return True
        if len(odd_degree_nodes) == 2:
            a = odd_degree_nodes[0]
            b = odd_degree_nodes[1]
            if a not in degree[b]:
                return True
            for c in range(1, n+1):
                if c != a and c != b and c not in degree[a] and c not in degree[b]:
                    return True
        if len(odd_degree_nodes) == 4:
            for a,b,c,d in [0,1,2,3], [0,2,1,3], [0,3,1,2]:
                a = odd_degree_nodes[a]
                b = odd_degree_nodes[b]
                c = odd_degree_nodes[c]
                d = odd_degree_nodes[d]
                if a not in degree[b] and c not in degree[d]:
                    return True
        return False