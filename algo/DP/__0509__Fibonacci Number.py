class Solution:
    
    # 2022/03/09 
    # DP with memory optimization [O(n): 95% / O(1): 73%]
    def fib(self, N: int) -> int:
        print("Code2")
        if N < 2:
            return N
        dp0, dp1, cur = 0, 1, 0
        for i in range(2, N+1):
            cur = dp0 + dp1
            dp0 = dp1
            dp1 = cur
        return cur
    
    # 2022/03/09 
    # DP [O(n): 88% / O(n): 42%]
    def fib1(self, N: int) -> int:
        print("Code1")
        if N < 2:
            return N
            
        dp = [0] * (N+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]