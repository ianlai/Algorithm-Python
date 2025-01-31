class Solution:
    
    # DP [O(n): 96%]
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1],[1,1]]
        if numRows == 1:
            return [dp[0]]        
        if numRows == 2:
            return dp
            
        for i in range(2, numRows):
            dp.append([0] * (i + 1))
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = 1
                elif j == i: 
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 
        
        return dp