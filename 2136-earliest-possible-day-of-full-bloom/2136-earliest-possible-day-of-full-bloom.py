class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
#         1+2 2+3 3+1
#         3   5   4
        
        
#         (3, 1,2), (3, 2,1), (5, 3,2), (3, 2,1)
#         0           1           2       3
        
#         0   1   2   3   4   5   6   7   8   9   10  11  12  13
#         2   2   2           D
#                     0           D
#                         1   1       D
#                                 3   3       D

#         [3,1,2], [7,4,3], [4,3,1]
        
#         [4,3], [3,1], [1,2]
        
        arr = [[x, y] for x, y in zip(plantTime, growTime)]
        arr.sort(key= lambda x: -x[1])
        n = len(arr)
        
        
        gtime = [arr[0][0]]
        btime = [arr[0][1]]
        for i in range(1, n):
            gtime.append(arr[i][0] + gtime[i-1])
            btime.append(arr[i][1])
            
        return max(x+y for x, y in zip(gtime, btime))