DEBUG = False
class Solution:
    
    # DFS to chagne island1 ; BFS to find min path to island2 [5%]
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.minFlip = float('inf')
        
        self.printGrid(grid)
        self.convertFirstIsland(grid)
        
        self.printGrid(grid)
        self.findMinFromFirstIsland(grid)
        
        self.printGrid(grid)
        
        return self.minFlip
    
    def convertFirstIsland(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfsChange(grid, i, j) #change to (2)
                    return 
                
    def dfsChange(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n:
            if grid[i][j] == 1:
                grid[i][j] = 2
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    self.dfsChange(grid, ni, nj)
                    
    def findMinFromFirstIsland(self, grid):
        m, n = len(grid), len(grid[0])
        dis = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    minDis = float('inf')
                    
                    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        #self.dfsFind(grid, ni, nj, 0, dis) #find island2 (1) 
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        minDis = min(minDis, self.bfsFind(grid, ni, nj)) #find island2 (1)
                        
                    dis[i][j] = minDis
                    self.minFlip = min(self.minFlip, minDis)
                    
    # OK
    def bfsFind(self, grid, row, col):
        m, n = len(grid), len(grid[0])
        deq = collections.deque([(row, col)])
        distance = {(row, col) : 0}
        while deq: 
            (i, j) = deq.popleft()
            if grid[i][j] == 1: 
                return distance[(i, j)] 
            if grid[i][j] == 2:
                continue
                
            # prune
            if distance[(i, j)] >= self.minFlip:
                return distance[(i, j)]
            
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if (ni, nj) in distance: 
                    continue
                distance[(ni, nj)] = distance[(i, j)] + 1
                deq.append((ni, nj))
        return float('inf')    
            
    # Failed
    def dfsFind(self, grid, i, j, distance, dis):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n:

            if grid[i][j] == 2: #island-1
                return 
        
            if grid[i][j] == 0: #sea
                distance += 1
                
                if distance > dis[i][j]:
                    return 
                else:
                    dis[i][j] = distance

                #grid[i][j] = 3 #visited
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    self.dfsFind(grid, ni, nj, distance, dis)
                #grid[i][j] = 0 #backtracking 

            if grid[i][j] == 1: #island-2
                self.minFlip = min(self.minFlip, distance)
                return 
            
    def printGrid(self, grid):
        if not DEBUG:
            return 
        print("----------")
        for row in grid:
            print(row)
            
                