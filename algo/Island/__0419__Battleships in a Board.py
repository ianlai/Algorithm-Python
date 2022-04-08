class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m, n = len(board), len(board[0])
        
        def dfs(row, col):
            if not(0 <= row < m and 0 <= col < n):
                return 
            if board[row][col] == ".":
                return 
            board[row][col] = "."
            
            for ni, nj in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(ni, nj)
            
                
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    dfs(i, j)
                    count += 1
        return count 