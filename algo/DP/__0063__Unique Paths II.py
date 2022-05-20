class Solution:
    
    # 2022/05/20 
    # DP [O(MN): 37% / O(MN): 42%]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        print("Code2")
        A = obstacleGrid
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m)]
        if A[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        

        
        
    # 2021/06/25 
    # DP
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        print("Code1")
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