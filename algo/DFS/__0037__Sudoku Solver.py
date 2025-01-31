class Solution:
    
    # 2022/04/17
    # Backtracking [Time: O(9 ^ space): 20% / Space: O(recursion level + blanks) = O(81) = O(1): 25%]
    def solveSudoku(self, board: List[List[str]]) -> None:
        print("Code2")
        if not board or not board[0]:
            return 
        m, n = len(board), len(board[0])
        
        def collectBlanks():
            blanks = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == ".":
                        blanks.append([i, j])
            return blanks
        
        def backtracking(blanks, idx, cur):
            if len(cur) == len(blanks):
                return True
            
            for number in range(1, 10):
                number = str(number)
                row, col = blanks[idx]
                if not isValid(row, col, number):
                    continue
                    
                board[row][col] = str(number)
                cur.append(number)
                if backtracking(blanks, idx + 1, cur):
                    return True
                cur.pop()
                board[row][col] = "."
                
        def isValid(row, col, number):
            #check row
            rowSet = set()
            for i in range(9):
                rowSet.add(board[row][i])
            if number in rowSet:
                return False
            
            #check col
            colSet = set()
            for i in range(9):
                colSet.add(board[i][col])
            if number in colSet:
                return False
            
            #check block 
            rowOut = row // 3
            colOut = col // 3
            blockSet = set()
            for i in range(3):
                for j in range(3):
                    blockSet.add(board[rowOut * 3 + i][colOut * 3 + j])
            if number in blockSet:
                return False
            return True
        
        blanks = collectBlanks()
        filledBlanks = []
        backtracking(blanks, 0, filledBlanks)
        return 
         
        

    # 2021/11/02 
    # DFS [O(9^b), 5%] ; b is number of blank
    # 有兩種座標，原始的二維矩陣座標(i, j) = val，或有數值才放入的一維矩陣list (i, j , val)
    # 一開始先計算有哪些空白，這樣才能使用index來做前進和回溯
    # 最後要提前跳出，這裡使用isDone的list來紀錄flag。否則填入的數值又被backtrack掉，會得到原本的board
    
    def solveSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("Code1")
        if not board or not board[0]:
            return 
        
        blanks = self.getBlanks(board)
        print("# of blanks:", len(blanks))
        
        isDone = [False]
        self.dfs(board, blanks, 0, [], isDone)
        return 

    def getBlanks(self, board):
        blanks = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    blanks.append((i, j))
        return blanks
    
    def dfs(self, board, blanks, idx, cur, isDone):
        if len(cur) == len(blanks):
            ### Debug: 
            # print("OUT!!", len(cur))
            # for i in range(len(cur)):
            #     if i > 0 and cur[i][0][0] != cur[i-1][0][0]:
            #         print()
            #     print(cur[i], end = "")
            # print()
            isDone[0] = True
            return 
        
        curBlank = blanks[idx]
        for i in range(9):
            val = i + 1
            if not self.isValid(board, curBlank, val): #cur (filled list) doesn't need to be passed in (board is updated on the fly)
                continue
            stashVal = board[curBlank[0]][curBlank[1]] #store the old value
            
            cur.append((curBlank, val)) 
            board[curBlank[0]][curBlank[1]] = str(val)
            self.dfs(board, blanks, idx + 1, cur, isDone)
            if isDone[0] == True:                      #avoid backtracking after the whole process is done 
                return  
            board[curBlank[0]][curBlank[1]] = stashVal
            cur.pop()
        return 
    
    def isValid(self, board, curBlank, curVal):
        
        #print(curVal)
        
        I = curBlank[0]
        J = curBlank[1]
        
        #=== Check row ===
        arr = [0] * 9
        for k in range(9):
            if not board[I][k].isdigit():
                continue
            val = int(board[I][k]) 
            arr[val - 1] = 1
        if arr[curVal - 1] == 1:
            #print("fail row check; ", arr, curVal)
            return False
        #print("pass row check")
        
        #=== Check col ===
        arr = [0] * 9
        for k in range(9):
            if not board[k][J].isdigit():
                continue
            val = int(board[k][J]) 
            arr[val - 1] = 1
        if arr[curVal - 1] == 1:
            #print("fail row check; ", arr, curVal)
            return False
        #print("pass col check")   
        
        #=== Check block ===
        arr = [0] * 9
        if 0 <= I < 3:
            blockI = 0 
        elif 3 <= I < 6:
            blockI = 3
        elif 6 <= I < 9:
            blockI = 6
        if 0 <= J < 3:
            blockJ = 0 
        elif 3 <= J < 6:
            blockJ = 3
        elif 6 <= J < 9:
            blockJ = 6
            
        for k in range(9):            
            row = blockI + k // 3
            col = blockJ + k % 3
            if not board[row][col].isdigit():
                continue
            val = int(board[row][col]) 
            arr[val - 1] = 1
        if arr[curVal - 1] == 1:
            #print("fail block check")
            return False
        #print("pass block check")
        return True
        
    def printBoard(self, board):
        for row in board:
            print(row)