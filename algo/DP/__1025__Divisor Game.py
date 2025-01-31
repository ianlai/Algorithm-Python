class Solution:
    
    #Math [60%]
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
    
    #DP [5%]
    def divisorGame1(self, n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        if n == 3: 
            return False
        
        dp = [0] * (n+1)
        dp[1] = False
        dp[2] = True
        dp[3] = False
        for i in range(4, n+1):
            win = False
            for j in range(1, i):
                if i % j == 0 and not dp[i-j]:
                    win = True
                    continue
            dp[i] = win
        return dp[n]