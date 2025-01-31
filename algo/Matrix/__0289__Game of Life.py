class Solution:
    
    # 2022/04/12
    # Matrix manipulation [Time O(m*n): 63% / Space O(1): 12%]
    # Save the previous states in values 
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("Code3")
        def countNeighbor(board, i, j):
            count = 0
            for ni in [i-1, i, i+1]:
                if not 0 <= ni < m:
                    continue
                for nj in [j-1, j, j+1]:
                    if ni == i and nj == j:
                        continue
                    if not 0 <= nj < n:
                        continue
                    if board[ni][nj] == 0 or board[ni][nj] == 2:
                        continue
                    count += 1
            return count 
                    
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = countNeighbor(board, i, j)
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 2  #changed
                else:
                    if count < 2:
                        board[i][j] = -1
                    elif count == 2 or count == 3:
                        board[i][j] = 1 #changed
                    elif count > 3:
                        board[i][j] = -1
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0
                        
    # ======================================================== 
    # 2022/04/12
    # Matrix manipulation [Time O(m*n):63% / Space O(m*n):51%]
    # Not copy the matrix back, copy in the beginning (might be faster?)
    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("Code2")
        def countNeighbor(board, i, j):
            count = 0
            for ni in [i-1, i, i+1]:
                if not 0 <= ni < m:
                    continue
                for nj in [j-1, j, j+1]:
                    if ni == i and nj == j:
                        continue
                    if not 0 <= nj < n:
                        continue
                    count += board[ni][nj]
            return count 
                    
        m, n = len(board), len(board[0])
        copyBoard = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = countNeighbor(copyBoard, i, j)
                if copyBoard[i][j] == 0:
                    if count == 3:
                        board[i][j] = 1
                else:
                    if count < 2:
                        board[i][j] = 0
                    elif count == 2 or count == 3:
                        board[i][j] = 1
                    elif count > 3:
                        board[i][j] = 0
                        
    # ========================================================
    # 2022/04/12
    # Matrix manipulation [Time O(m*n):63% / Space O(m*n):51%]
    # Copy the matrix back (slower)
    def gameOfLife1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("Code1")
        def countNeighbor(board, i, j):
            count = 0
            for ni in [i-1, i, i+1]:
                if not 0 <= ni < m:
                    continue
                for nj in [j-1, j, j+1]:
                    if ni == i and nj == j:
                        continue
                    if not 0 <= nj < n:
                        continue
                    count += board[ni][nj]
            return count 
                    
        m, n = len(board), len(board[0])
        nextBoard = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = countNeighbor(board, i, j)
                if board[i][j] == 0:
                    if count == 3:
                        nextBoard[i][j] = 1
                else:
                    if count < 2:
                        nextBoard[i][j] = 0
                    elif count == 2 or count == 3:
                        nextBoard[i][j] = 1
                    elif count > 3:
                        nextBoard[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                board[i][j] = nextBoard[i][j]