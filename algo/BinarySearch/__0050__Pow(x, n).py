class Solution:
    
    # Faster Iterative [O(logn), 80%]
    def myPow(self, x: float, n: int) -> float:
        print("Fast Iterative")
        if n == 0:
            return 1
        
        positive = True
        if n < 0:
            positive = False
        n = abs(n)
        
        ans = x
        
        # Make sure n is even 
        nIsOdd = False

        side = 1 
        while n != 1:
            #print(ans, n, side)
            if n % 2 == 1:
                n -= 1
                side = ans * side
            else:
                ans = ans * ans 
                n = n // 2
        ans = ans * side
        
        return ans if positive == True else 1/ans
    
    # Naive Iterative [O(n), TLE]
    def myPow2(self, x: float, n: int) -> float:
        print("Iterative")
        if n == 0:
            return 1
        
        positive = True
        if n < 0:
            positive = False
        n = abs(n)
        
        ans = 1 
        for i_ in range(n):
            ans *= x
        return ans if positive == True else 1/ans  
    
    # Math [94%]
    def myPow1(self, x: float, n: int) -> float:
        print("Math")
        return x ** float(n)