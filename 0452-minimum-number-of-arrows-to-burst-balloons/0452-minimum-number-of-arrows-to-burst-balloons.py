class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
        # ---------------------
        #     -------------------------
        #                                     --------------------------
        #                         ----------------------
        
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