class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_height = abs(ay1 - ay2)
        a_width = abs(ax1 - ax2)
        a_area = a_height * a_width
        
        b_height = abs(by1 - by2)
        b_width = abs(bx1 - bx2)
        b_area = b_height * b_width
        
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        common_width = (right - left)
        
        bottom = max(ay1, by1)
        top = min(ay2, by2)
        common_height = (top - bottom)
        
        common_area = common_height * common_width if (common_height > 0 and common_width > 0) else 0
        
        return a_area + b_area - common_area