class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
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