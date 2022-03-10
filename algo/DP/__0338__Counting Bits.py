class Solution:
    
    # 2022/03/10
    # DP [O(n): 86%]
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0] 
        dp = [0, 1]
        while len(dp) < n + 1:
            for i in range(len(dp)):
                dp.append(dp[i] + 1)
        return dp[:n+1]