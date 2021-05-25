class Solution:
    
    # DFS [O(n2), 30%]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, self.dfs(grid, i, j))
        return maxSize
                    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return 0
        if j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        size = 1 
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in dirs:
            nextI = i + d[0]
            nextJ = j + d[1]
            size += self.dfs(grid, nextI, nextJ)
        return size