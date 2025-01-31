class Solution:
    
    #DFS [O(n!), 17%]
    def totalNQueens(self, n: int) -> int:
        if n <= 0:
            return 0
        
        results = []
        self.dfs(n, 0, [], results)
        print(results)
        return len(results)
        #return results[0]
    
    def dfs(self, n, row, cur, results):
        if row == n:
            results.append(list(cur)) #Store all methods
            #results[0] +=1       #Store the number of methods only
            return 
        
        for i in range(n):
            nextPos = (row, i)  
            if not self.isValid(cur, nextPos[0], nextPos[1]):
                continue 
            cur.append(nextPos) #add row in this layer, starting from 0
            self.dfs(n, row + 1, cur, results) 
            cur.pop()
        
    def isValid(self, cur, row, col):
        for pos in cur:
            if pos[0] == row:  #not needed
                return False
            if pos[1] == col:
                return False
            if pos[0] + pos[1] == row + col:
                return False
            if pos[0] - pos[1] == row - col:
                return False
        return True
            
    