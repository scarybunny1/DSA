class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
        # ---------------------
        #     -------------------------
        #                                     --------------------------
        #                         ----------------------
        
        points.sort(key= lambda x: x[1])
        curr_end = points[0][1]
        arrows = 1
        for i in range(1, len(points)):
            if points[i][0] > curr_end:
                arrows += 1
                curr_end = points[i][1]
        return arrows
            
        
        def overlaps(i1, i2):
            return min(i1[1], i2[1]) - max(i1[0], i2[0]) >= 0
                
        stack = []
        points.sort(key=lambda x: x[1])
        
        for point in points:
            if stack and overlaps(stack[-1], point):
                prev_point = stack.pop()
                new_point = [max(point[0], prev_point[0]), min(point[1], prev_point[1])]
                stack.append(new_point)
            else:
                stack.append(point)
        
        return len(stack)
    
        