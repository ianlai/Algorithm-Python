class Solution:
    
    # Memoization DP [O(n*n*k): 53%]
    # 計算方式是就算失敗，後面的計數也都要開展出來。
    # 假設 第一步有2種成功，之後第二步又各再有兩種。
    # 正確計算: (2+2) / 8*8    
    # 錯誤計算: (2+2) / (6+8+8)
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        memo = {}
        inCount = self.dfs(n, k, row, col, memo)
        return inCount / 8**k
        
    def dfs(self, n, k, row, col, memo): 
        if not (0 <= row < n) or not (0 <= col < n):
            return 0
        if k == 0:
            return 1
        if (row, col, k) in memo:
            return memo[(row, col, k)]

        moveList = [(row+2, col+1), 
                    (row-2, col+1), 
                    (row+2, col-1), 
                    (row-2, col-1), 
                    (row+1, col+2), 
                    (row-1, col+2), 
                    (row+1, col-2), 
                    (row-1, col-2)]
        inCount = 0
        for nr, nc in moveList:
            inCount += self.dfs(n, k-1, nr, nc, memo)
        memo[(row, col, k)] = inCount
        return inCount 
    
    
#     def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        
#         inCount, totalCount = self.dfs(n, k, row, col)
#         print(inCount, totalCount, inCount/totalCount)
#         return inCount/totalCount
        
#     def dfs(self, n, k, row, col): 
        
#         if not (0 <= row < n):
#             return 0, 1
            
#         if not (0 <= col < n):
#             return 0, 1
                
#         if k == 0:
#             return 1, 1
            
#         moveList = [(row+2, col+1), (row-2, col+1), (row+2, col-1), (row-2, col-1), (row+1, col+2), (row-1, col+2), (row+1, col-2), (row-1, col-2)]
#         inCount, totalCount = 0, 0
#         for nr, nc in moveList:
#             count = self.dfs(n, k-1, nr, nc)
#             inCount += count[0]
#             totalCount += count[1]
#         return inCount, totalCount 