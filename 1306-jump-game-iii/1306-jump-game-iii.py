class Solution:
    def checkPossibility(self, index, arr, n, visited):
        if not (0 <= index < n and index not in visited):
            return False
        visited.add(index)
        if arr[index] == 0:
            return True
        
        if self.checkPossibility(index + arr[index], arr, n, visited):
            return True
        
        if self.checkPossibility(index - arr[index], arr, n, visited):
            return True
        
        
    
    def canReach(self, arr: List[int], start: int) -> bool:
        """BFS"""
#         q = collections.deque([start])
#         visited = set()
#         n = len(arr)
#         while q:
#             pos = q.popleft()
#             if arr[pos] == 0:
#                 return True
#             if pos in visited:
#                 continue
#             visited.add(pos)
            
#             if pos + arr[pos] < n:
#                 q.append(pos+arr[pos])
            
#             if pos - arr[pos] >= 0:
#                 q.append(pos-arr[pos])
#         return False
        """DFS"""
        return self.checkPossibility(start, arr, len(arr), set())