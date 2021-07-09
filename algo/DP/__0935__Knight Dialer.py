class Solution:
    def knightDialer(self, n: int) -> int:
        if n <= 0:
            return 0
        modBase = pow(10, 9) + 7 
        
        moveFromMap = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        dp = [[0 for _ in range(10)] for _ in range(2)]
        
        for j in range(10):
            dp[0][j] = 1
        
        for i in range(1, n): 
            for j in range(10):
                dp[i%2][j] = 0
                for k in moveFromMap[j]:
                    dp[i%2][j] += dp[(i-1)%2][k] % modBase
    
        return sum(dp[(n-1)%2]) % modBase