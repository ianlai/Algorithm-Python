MOD = 10 ** 9 + 7
class Solution:
    
    # 2022/01/25
    # Memoization DP [O(mnM): 71%]
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        print("Code2")
        def dfs(m, n, row, col, leftMove, memo):
            if not (0 <= row < m and 0 <= col < n):
                return 1
            if leftMove == 0:
                return 0
            if (row, col, leftMove) in memo:
                return memo[(row, col, leftMove)]
            
            count = 0 
            for n_row, n_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                count += dfs(m, n, n_row, n_col, leftMove - 1, memo)
            memo[(row, col, leftMove)] = count % MOD
            return memo[(row, col, leftMove)] 
        
        memo = {}
        return dfs(m, n, startRow, startColumn, maxMove, memo)
    
    # ===================================================
    
    # 2021/06/25 
    # Memoization DP 
    def findPaths1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        print("Code1")
        if m <= 0 or n <= 0:
            return 0
        memo = {}
        return self.dfs(m, n, maxMove, startRow, startColumn, memo) % (10 ** 9 + 7)
    
    def dfs(self, m, n, maxMove, r, c, memo):
        if (maxMove, r, c) in memo:
            return memo[(maxMove, r, c)]
        if not (0 <= r < m):
            return 1
        if not (0 <= c < n):
            return 1
        if maxMove <= 0:
            return 0
        
        count = 0
        for d in [[1,0], [-1,0], [0,1], [0,-1]]:
            next_r = r + d[0]
            next_c = c + d[1]
            count += self.dfs(m, n, maxMove - 1, next_r, next_c, memo)
        memo[(maxMove, r, c)] = count
        return count 