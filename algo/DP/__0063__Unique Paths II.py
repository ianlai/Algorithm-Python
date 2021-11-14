class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                    continue
                        
                if i == 0:
                    if obstacleGrid[i][j] == 1: 
                        dp[i][j] = 0
                    else:
                        dp[i][j] =  dp[i][j-1] 
                    continue
                        
                if j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] =  dp[i-1][j]
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        #for row in dp:
        #    print(row)
        return dp[-1][-1]