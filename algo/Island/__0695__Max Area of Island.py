class Solution:
    
    # BFS [O(n2), 74%]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        print("BFS")
        if not grid:
            return 0
    
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, self.bfs(grid, i, j))
        return maxSize
    
    def bfs(self, grid, i, j):
        deq = collections.deque([(i, j)])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        size = 1 
        grid[i][j] = 0 
        while deq:
            #print("---")
            for _ in range(len(deq)):
                cur = deq.popleft()
                #grid[cur[0]][cur[1]] = 0 
                #print(cur)
                for d in dirs:
                    nextI = cur[0] + d[0]
                    nextJ = cur[1] + d[1]
                    if nextI < 0 or nextI >= len(grid):
                        continue
                    if nextJ < 0 or nextJ >= len(grid[0]):
                        continue
                    if grid[nextI][nextJ] == 0:
                        continue
                    grid[nextI][nextJ] = 0  #Must set 0 before adding to deque, not after taking it out
                    deq.append((nextI, nextJ))
                    size += 1
        #print(i, j, size)
        return size
        
    # ======================================================
    
    # DFS, change the island to sea after visited [O(n2), 30% / Worst case: O(n2), 56%]
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        print("DFS")
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