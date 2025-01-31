class Solution:
    
    # 2022/04/22
    # DFS[Time: O(mn): 85% / Space: O(m): 59%]
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        def dfs(grid, col, i, j, res):
            if i == m:
                res[col] = j
                return 
            
            if grid[i][j] == 1 and j + 1 < n and grid[i][j+1] == 1:
                dfs(grid, col, i+1, j+1, res)
            
            if grid[i][j] == -1 and j - 1 >= 0 and grid[i][j-1] == -1:
                dfs(grid, col, i+1, j-1, res)
            
        res = [-1] * n
        for j in range(n):
            dfs(grid, j, 0, j, res)
        return res
            