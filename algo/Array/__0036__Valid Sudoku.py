class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board[0]) == 0:
            return False
        
        # === Debug ===
        # for row in board:
        #     print(row)
        
        if not self.validateRow(board):
            return False
        if not self.validateCol(board):
            return False
        if not self.validateBlock(board):
            return False
        return True
    
    def validateRow(self, board):
        n = len(board)
        for i in range(n):
            arr = [0] * n 
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                val = int(val) - 1   #digit to index
                if arr[val] == 1:
                    return False
                arr[val] = 1
        return True
        
    def validateCol(self, board):
        n = len(board)
        for j in range(n):
            arr = [0] * n 
            for i in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                val = int(val) - 1
                if arr[val] == 1:
                    return False
                arr[val] = 1
        return True
    
    def validateBlock(self, board):
        n = len(board)
        for i in range(n):
            arr = [0] * n 
            for j in range(n):
                innerRow = j // 3 
                innerCol = j % 3
                outerRow = i // 3
                outerCol = i % 3
                x = outerRow * 3 + innerRow 
                y = outerCol * 3 + innerCol
                val = board[x][y]
                if val == ".":
                    continue
                val = int(val) - 1   #digit to index
                if arr[val] == 1:
                    return False
                arr[val] = 1
        return True