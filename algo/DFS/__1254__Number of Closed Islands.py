class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if visited[i][j] == 1:
                    continue
                if grid[i][j] == 1: #water 
                    continue
                    
                if self.dfs(grid, visited, i, j):
                    count += 1
        return count
    
    def dfs(self, grid, visited, i, j):
        
        m = len(grid)
        n = len(grid[0])
        
        if not (0 <= i < m and 0 <= j < n): #out of boundary -> nok
            return False
        if grid[i][j] == 1:     #land -> ok
            return True
        if visited[i][j] == 1:  #visited -> ok
            return True
        
        visited[i][j] = 1
        
        returnVal = True
        for di, dj in [(1, 0), (-1,0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            returnVal &= self.dfs(grid, visited, ni, nj)
        return returnVal 