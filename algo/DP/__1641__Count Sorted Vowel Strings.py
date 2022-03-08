class Solution:
    
    # 2022/03/08
    # DP [O(n): 68%]
    # 看起來不難，但需要兩個dp matrix(或省空間的array)，但還是想很久才找出關係式子
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 5 + 4 + 3 + 2 + 1
        
        dp = [[1 for _ in range(5)] for _ in range(n)]
        pascal = [[1 for _ in range(5)] for _ in range(n)]
        total = sum(dp[0])
        
        for i in range(2, n):
            for j in range(5):
                if j == 0:
                    pascal[i][j] = pascal[i-1][j]
                else:
                    pascal[i][j] = pascal[i][j-1] + pascal[i-1][j]
                dp[i][j] = pascal[i][j] * (5 - j)
                
        return sum(dp[n-1])
            