class Solution:
    
    # 2022/04/03 
    # Conciser [O(1): 88%]
    def tictactoe(self, moves: List[List[int]]) -> str:
        print("Code2")
        grid = [[0 for _ in range(3)] for _ in range(3)]
        def setAndCheck(grid, row, col, val):
            grid[i][j] = val
            if grid[0][col] == grid[1][col] == grid[2][col] == val:
                return val
            if grid[row][0] == grid[row][1] == grid[row][2] == val:
                return val
            if row == col and grid[0][0] == grid[1][1] == grid[2][2] == val:
                return val
            if row + col == 2 and grid[2][0] == grid[1][1] == grid[0][2] == val:
                return val
            return 0
            
        step = 0
        for i, j in moves:
            if step % 2 == 0:
                res = setAndCheck(grid, i, j, "A")
            else:
                res = setAndCheck(grid, i, j, "B")
            if res != 0:
                return res
            step += 1
            
        if step == 9:
            return "Draw"
        else:
            return "Pending"
    # ==========================
    # 2022/04/01 
    # Verbose, using for loops [O(1): 45%]
    def tictactoe(self, moves: List[List[int]]) -> str:
        print("Code1")
        grid = [[0 for _ in range(3)] for _ in range(3)]
        
        def check(grid, row, col, val):
            for i in range(3):
                if grid[i][col] != val:
                    break
                if i == 2:
                    return val
            
            for i in range(3):
                if grid[row][i] != val:
                    break
                if i == 2:
                    return val
                
            if row == col: 
                for i in range(3):
                    if grid[i][i] != val:
                        break
                    if i == 2:
                        return val
            
            if row + col == 2: 
                for i in range(3):
                    if grid[i][2-i] != val:
                        break
                    if i == 2:
                        return val
            return 0
            
            
        step = 0
        for i, j in moves:
            #print("s:", step)
            if step % 2 == 0:
                grid[i][j] = 1
                res = check(grid, i, j, 1)
                #print(res)
                if res == 1:
                    return "A"
                elif res == 2:
                    return "B"
                    
            else:
                grid[i][j] = 2
                res = check(grid, i, j, 2)
                #print(res)
                if res == 1:
                    return "A"
                elif res == 2:
                    return "B"
            step += 1
            
        if step == 9:
            return "Draw"
        else:
            return "Pending"