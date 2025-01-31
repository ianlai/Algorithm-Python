'''
2022/05/28 
'''
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        print("Code3 (BEST)")
        self.len  = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagR = 0
        self.diagL = 0
    
    # Record score only (player1, player2) [O(1): 25% / O(N): 21%]
    def move(self, row: int, col: int, player: int) -> int:
        curPlayer = 1 if player == 1 else -1
        
        # set row and col 
        self.rows[row] += curPlayer
        self.cols[col] += curPlayer
        
        # set diagonal 
        if row == col:
            self.diagR += curPlayer
                
        if row + col + 1 == self.len:
            self.diagL += curPlayer
        
        # check 
        if abs(self.rows[row]) == self.len:
            return player
        
        if abs(self.cols[col]) == self.len:
            return player
            
        if abs(self.diagR) == self.len:
            return player
        
        if abs(self.diagL) == self.len:
            return player
            
        return 0

'''
2022/05/28 
'''
class TicTacToe2:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        print("Code2")
        self.len  = n
        self.row  = [[0, 0] for _ in range(n)]   #player1, filled
        self.col  = [[0, 0] for _ in range(n)] 
        self.digR = [0, 0]
        self.digL = [0, 0]
    
    # Record count only (player1, filled) [O(1): 74% / O(N): 51%]
    def move(self, row: int, col: int, player: int) -> int:
        
        # set row and col 
        self.row[row][1] += 1
        self.col[col][1] += 1   
        
        if player == 1:
            self.row[row][0] += 1
            self.col[col][0] += 1
        
        # set diagonal 
        if row == col:
            self.digR[1] += 1
            if player == 1:
                self.digR[0] += 1
                
        if row + col + 1 == self.len:
            self.digL[1] += 1
            if player == 1:
                self.digL[0] += 1
        
        # check 
        if self.row[row][1] == self.len:
            if self.row[row][0] == self.len or self.row[row][0] == 0:
                return player
        
        if self.col[col][1] == self.len:
            if self.col[col][0] == self.len or self.col[col][0] == 0:
                return player
            
        if self.digR[1] == self.len:
            if self.digR[0] == self.len or self.digR[0] == 0:
                return player
        
        if self.digL[1] == self.len:
            if self.digL[0] == self.len or self.digL[0] == 0:
                return player
            
        return 0

'''
2022/05/28 
'''
class TicTacToe1:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        print("Code1")
        self.board = [[None] * n for _ in range(n)]
        self.len = n
        
    # Optimized brute-force, check current row and col  [O(N): 14% / O(N2): 21%]
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        assert self.board[row][col] is None
        
        # set 
        self.board[row][col] = player
        
        # check row 
        rowCount = 0
        for i in range(self.len):
            if self.board[i][col] is None: #not done yet
                break 
            if self.board[i][col] == player:
                rowCount += 1
        if rowCount == self.len:
            return player
        
        # check col
        colCount = 0
        for i in range(self.len):
            if self.board[row][i] is None: #not done yet
                break 
            if self.board[row][i] == player:
                colCount += 1
        if colCount == self.len:
            return player
        
        # check diagonal right 
        if row == col:
            diagCountRight = 0 
            for i in range(self.len):
                if self.board[i][i] is None: #not done yet
                    break 
                if self.board[i][i] == player:
                    diagCountRight += 1
            if diagCountRight == self.len:
                return player
        
        # check diagonal left 
        if row + col + 1 == self.len:
            diagCountLeft = 0 
            for i in range(self.len):
                if self.board[i][self.len - 1 - i] is None: #not done yet
                    break 
                if self.board[i][self.len - 1 - i] == player:
                    diagCountLeft += 1
            if diagCountLeft == self.len:
                return player
            
        return 0 
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)