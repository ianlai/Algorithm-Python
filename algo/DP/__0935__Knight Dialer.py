modBase = 10 ** 9 + 7 
class Solution:
    
    # 2022/05/10
    # DP (space optimization by two lists) [O(10*N*3): 59% / O(10*2): 84%]
    def knightDialer(self, n: int) -> int:
        print("Code2")
        nToN = {
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
        dpRow1 = [1] * 10
        dpRow2 = [0] * 10
        
        if n == 1: 
            return 10
        
        for i in range(1, n):
            dpRow2 = [0] * 10
            for j in range(10):
                for pre in nToN[j]:
                    dpRow2[j] += dpRow1[pre] % modBase
            dpRow1 = dpRow2
        return sum(dpRow2) % modBase

            
    # 2021/07/09 
    # DP (space optimization by mod) [O(10*N*3)=O(N): 50% / O(10*2)=O(1): 84%]
    def knightDialer1(self, n: int) -> int:
        print("Code1")
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