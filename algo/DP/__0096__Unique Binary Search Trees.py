class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n + 1) 
        dp[0] = 1 
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(1, i+1):
                l = j - 1
                r = i - j
                if l > 0 and r <= n:
                    add = dp[l] * dp[r]
                elif l > 0:
                    add = dp[l]
                elif r <= n:
                    add = dp[r]
                dp[i] += add
        return dp[n]