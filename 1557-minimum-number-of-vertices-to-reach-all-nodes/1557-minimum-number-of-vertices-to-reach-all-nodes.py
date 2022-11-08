class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        for node, neighbor in edges:
            indegree[neighbor] += 1
            
        ans = []
        for node, degree in enumerate(indegree):
            if degree == 0:
                ans.append(node)
        return ans