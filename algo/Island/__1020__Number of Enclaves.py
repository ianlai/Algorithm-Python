class Solution:
    
    # Assume grid is immutable 
    # BFS, adding a matrix to record the island connecting to boundaries [O(n): 64%]
    def numEnclaves(self, grid: List[List[int]]) -> int:
        print("Method-2")
        def dfs(i, j):
            if grid[i][j] != 1:
                return 
            if boundaryIslands[i][j] == 1:
                return 
            boundaryIslands[i][j] = 1
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    dfs(ni, nj)
        # Initialize     
        m, n = len(grid), len(grid[0])
        boundaryIslands = [[0 for j in range(n)]for i in range(m)]
        
        # DFS
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
            
        # Count 
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and boundaryIslands[i][j] == 0:
                    count += 1
        return count
        
    # ========================================= 
    # BFS, change land to 0 [O(n): 89%]
    def numEnclaves1(self, grid: List[List[int]]) -> int:
        print("Method-1-v2")
        def dfs(i, j):
            if grid[i][j] != 1:
                return
            grid[i][j] = 0 
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (0 <= ni < m and 0 <= nj < n):
                    dfs(ni, nj)

        m, n = len(grid), len(grid[0])
        
        #DFS starts from the boundaries
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
            
        #Count results
        count = 0
        for i in range(m):
            count += grid[i].count(1)
        return count  
    
    # =========================================
    
    # BFS, adding visited array, but it's not needed [X]
    def numEnclaves(self, grid: List[List[int]]) -> int:
        print("Version-1")
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