class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if grid[i][j] != 1:
                return
            grid[i][j] = 0 
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] != 1:
                    continue
                if (ni, nj) in visited:
                    continue
                visited.add((ni, nj))
                dfs(ni, nj, visited)

        m, n = len(grid), len(grid[0])
        visited = set()
        
        #Init
        for i in range(m):
            dfs(i, 0, visited)
            dfs(i, n-1,visited)
        for j in range(n):
            dfs(0, j, visited)
            dfs(m-1, j, visited)
            
        #Count
        count = 0
        for i in range(m):
            count += grid[i].count(1)

        return count        