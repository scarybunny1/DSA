class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def calculateArea(x1, y1, x2, y2):
            return (x2-x1) * (y2-y1)
        
        corners = set()
        total_area = 0
        
        for x1, y1, x2, y2 in rectangles:
            total_area += calculateArea(x1, y1, x2, y2)
            
            for x, y in [x1, y2], [x2, y1], [x1, y1], [x2, y2]:
                if (x, y) in corners:
                    corners.remove((x, y))
                else:
                    corners.add((x, y))
                    
        if len(corners) != 4:
            return False
        
        bottom_x, bottom_y = min(corners, key= lambda x: x[0] + x[1])
        top_x, top_y = max(corners, key= lambda x: x[0] + x[1])
        
        return calculateArea(bottom_x, bottom_y, top_x, top_y) == total_area