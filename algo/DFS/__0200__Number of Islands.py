class Solution:

    # (1) Traversal: BFS
    # (2) Status: visited set
    # [O(m*n), 10%][O(m*n), 36%]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        self.count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    self.bfs(grid, i, j, visited)
        return self.count 
                    
    def bfs(self, grid, i, j, visited):
        self.count += 1 
        deq = collections.deque([(i, j)])
        #print(i, j)
        while deq:
            
            cur = deq.popleft()
            for d in [(1, 0), (-1,0), (0, 1), (0,-1)]:
                nextI = cur[0] + d[0]
                nextJ = cur[1] + d[1]
                if (nextI, nextJ) in visited:
                    continue
                if not(0 <= nextI < len(grid) and 0 <= nextJ < len(grid[0])):
                    continue
                if grid[nextI][nextJ] != "1":
                    continue
                #print(deq)
                visited.add((nextI, nextJ))
                deq.append((nextI, nextJ))

    # ========================================
    # (1) Traversal: DFS
    # (2) Status: change 1 to 0 after visited 
    # [O(m*n), 10%]
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    
    def dfs(self, grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return
            
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)