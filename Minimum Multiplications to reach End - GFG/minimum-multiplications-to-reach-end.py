#User function Template for python3
import collections
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        q = collections.deque([(0, start)])
        n = 100000
        distance = [float('inf')]*n

        while q:
            steps, node = q.popleft()
            
            if node == end:
                return steps
                
            for num in arr:
                new_node = (num * node) % n
                if 1 + steps < distance[new_node]:
                    distance[new_node] = steps + 1
                    q.append((distance[new_node], new_node))
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends