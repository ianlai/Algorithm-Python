class Solution:
    def mySqrt(self, x: int) -> int:
        
        start, end = 0, x
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid
        
        if end * end > x:
            return start
        return end
        
                