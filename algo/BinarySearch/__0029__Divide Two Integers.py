class Solution:
    
    # 2022/05/30
    # Binary Search (using multiplication) [O(logn): 36% / O(1): 76%]
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Edge cases
        if dividend == 0:
            return 0

        MAX = 2147483647
        MIN = -2147483648
        if dividend == MIN and divisor == -1:
            return MAX
        if dividend == MAX and divisor == 1:
            return MAX
        if dividend == MIN and divisor == 1:
            return MIN
        if dividend == MAX and divisor == -1:
            return -MAX
        
        # Deal with negative
        minus = True if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor > dividend:
            return 0 
        
        def multiply(a, b):
            res = 0
            for _ in range(a):
                res += b
            return res

        # Binary Search 
        start, end = 0, dividend + 1
        while start < end:
            mid = start + (end - start) // 2
            target = mid * divisor 
            #target = multiply(mid, divisor) #TLE
            if target == dividend:
                start = mid + 1
                break 
            elif target < dividend:
                start = mid + 1
            else:
                end = mid
        return start - 1 if not minus else - (start - 1)
                
                
            