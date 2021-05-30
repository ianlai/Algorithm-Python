class Solution:
    
    # DFS [O(n!), 27%] 
    # - 時間複雜度不是O(n^n)，因為每次可以選的位置都會少1
    # - 要在這圈做還是下一圈做，順序要搞清楚 
    #   (e.g. isValid, result creation, cur append, loop, cur backtrack)
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        
        results = []
        formmatedResults = []
        
        # Loop in each row with DFS
        for j in range(n):
            self.dfs(n, 0, j, [], results) #cur contains (i, j)
            
        # Draw the final answer 
        for result in results:
            formmatedResults.append(self.drawBoard(n, result))
        
        #print("Raw result:\n", results)
        #print("Formatted result:\n", formmatedResults)
        self.printBoard(formmatedResults)
        return formmatedResults
    
    def dfs(self, n, row, col, cur, results):
        #print("DFS", row, col, cur)
        if not self.isValid(n, row, col, cur):
            return 
        
        #Add first, then check whether it's the last row to create the result
        cur.append((row, col)) #<---Add 
        if row == n - 1:
            results.append(list(cur)) 
            #print(">> Got one", cur)
            #return  #Don't return 
        
        for j in range(n):    
            self.dfs(n, row + 1, j, cur, results)
        cur.pop() #<---Backtrack 
        
    def isValid(self, n, row, col, cur):
        for point in cur:
            if point[0] == row:
                return False
            if point[1] == col:
                return False
            if point[0] + point[1] == row + col:
                return False
            if point[0] - point[1] == row - col:
                return False
        return True
    
    def drawBoard(self, n, points):
        formattedResult = []
        template = ["."] * n
        for point in points:
            col = point[1]
            formattedRow = list(template)
            formattedRow[col] = "Q"
            formattedResult.append("".join(formattedRow))
        return formattedResult
    
    def printBoard(self, board):
        for row in board:
            print(row)