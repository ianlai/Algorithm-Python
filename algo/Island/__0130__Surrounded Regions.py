class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        m, n = len(board), len(board[0])
        
        # Find the O on the edges 
        for i in range(m):
            self.dfs(board, i, 0, "O", "T")
            self.dfs(board, i, n - 1, "O", "T")
        for j in range(n):
            self.dfs(board, 0, j, "O", "T")
            self.dfs(board, m - 1, j, "O", "T")
        
        # Find the O surrounded by X, flip them to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    self.dfs(board, i, j, "O", "X")
        
        # Find the T and flip them back to O
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, "T", "O")
        
        return 
    
    def dfs(self, board, i, j, setF, setT):
        m, n = len(board), len(board[0])
        if not (0 <= i < m and 0 <= j < n): 
            return 
        if board[i][j] != setF:
            return 
        board[i][j] = setT
        
        for (ni, nj) in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            self.dfs(board, ni, nj, setF, setT)
        return
        
        
        