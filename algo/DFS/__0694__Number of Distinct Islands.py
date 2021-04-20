class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        #Null check 
        if grid is None or len(grid) == 0:
            return 0
        
        islandToPoints = {}
        
        #Traverse the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandToPoints[(i, j)] = []
                    self.dfs(grid, i, j, islandToPoints, i, j)
        
        #Traverse the map to remove the redundancy 
        islandSet = set()
        for key in islandToPoints:
            islandSet.add(tuple(islandToPoints[key])) #use set to remove redundancy; use tuple to make the list hashable
            
        return len(islandSet)
        
        
    def dfs(self, grid, i, j, islandToPoints, beginI, beginJ):
        
        #Boundary check
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return
        
        if grid[i][j] == 1:
            
            # Flip the land to 0 
            grid[i][j] = 0
            self.dfs(grid, i-1, j, islandToPoints, beginI, beginJ)
            self.dfs(grid, i+1, j, islandToPoints, beginI, beginJ)  
            self.dfs(grid, i, j-1, islandToPoints, beginI, beginJ)        
            self.dfs(grid, i, j+1, islandToPoints, beginI, beginJ)
            
            #Add the land points to the first touching point so that we can check the redundancy later
            islandToPoints[(beginI, beginJ)].append((i-beginI, j-beginJ))
