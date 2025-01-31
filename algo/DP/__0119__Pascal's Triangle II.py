class Solution:
    
    # Bottom-Up DP [O(n2): 85%]
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]            
        
        m = rowIndex
        #dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        dp = [[0 for _ in range(m+1)] for _ in range(2)]
        
        # for i in range(m+1):
        #     dp[i%2][0] = 1
        # for i in range(m+1):
        #     dp[i%2][i] = 1
        
        dp[1][0] = 1
        dp[1][1] = 1
        
        for i in range(2, m+1):
            dp[i%2][0] = 1
            dp[i%2][i] = 1
            for j in range(1, i):
                dp[i%2][j] = dp[(i-1)%2][j-1] + dp[(i-1)%2][j]
            #print(i, dp[i%2])
        
        return dp[m%2]