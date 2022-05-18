class Solution:
    
    # Math [O(1): 36% / O(1): 68%]
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        dx = min(ax2, bx2) - max(ax1, bx1)
        dy = min(ay2, by2) - max(ay1, by1)
        area3 = 0
        if dx > 0 and dy > 0:
            area3 = dx * dy        
        return area1 + area2 - area3