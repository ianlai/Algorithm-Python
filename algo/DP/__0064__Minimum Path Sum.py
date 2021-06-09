class Solution:
    #Bottom-up DP with rolling array [O(n2)/O(n), 33%/91%]
    def minPathSum(self, grid: List[List[int]]) -> int:
        print("Bottom-up DP2")
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(2)]
        #dp2 = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i%2][j] = dp[i%2][j-1] + grid[i][j]
                    #dp2[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i%2][j] = dp[i%2-1][j] + grid[i][j]
                    #dp2[i][j] = dp2[(i-1)][j] + grid[i][j]
                else:
                    dp[i%2][j] = min(dp[i%2-1][j], dp[i%2][j-1]) + grid[i][j]
                    #dp2[i][j] = min(dp2[(i-1)][j], dp2[i][j-1]) + grid[i][j]
        #     print(">", i, dp[i%2])
        # for i in range(m):
        #     print(dp2[i])
        # print("---")
        #for i in range(2):
        #    print(dp[i])
        
        if m % 2 == 0:
            return dp[1][n-1]
        else:
            return dp[0][n-1]
            
        #return max(dp[0][n-1], dp[1][n-1])
    
    # ==============================================
    #Bottom-up DP [O(n2)/O(n2), 41%/34%]
    def minPathSum1(self, grid: List[List[int]]) -> int:
        print("Bottom-up DP")
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]