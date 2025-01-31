class Solution:
    
    # Math [Time O(1): 86%]
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def distance(p1, p2): 
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        def mid(p1, p2):
            x = (p1[0] + p2[0]) / 2 
            y = (p1[1] + p2[1]) / 2
            return [x, y]
        
        # Any points the same -> False
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        # Center to 4 vertex different -> False (Might be rectengle even if it is True)
        m12 = mid(p1, p2)
        m34 = mid(p3, p4)
        m13 = mid(p1, p4)
        m24 = mid(p2, p4)
        m1234 = mid(m12, m34)
        
        d1 = distance(m1234, p1)
        d2 = distance(m1234, p2)
        d3 = distance(m1234, p3)
        d4 = distance(m1234, p4)
        
        if d1 != d2 or d1 != d3 or d1 != d4:
            return False
        
        # All two edges from p1 are different -> False 
        d12 = distance(p1, p2)
        d13 = distance(p1, p3)
        d14 = distance(p1, p4)
        if d12 != d13 and d12 != d14 and d13 != d14:
            return False
        
        return True