class Solution:
    
    # DP [O(n2): 65%]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # dp 
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
                dp[i][j] += matrix[i][j]

        return min(dp[n-1])