# 934. Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/

DEBUG = True
class Solution:
    
    
    # 2021/09/06
    # BFS starting with island2 [O(mn):62%] 
    # BFS一開始就把一整個島放進去開始，而不是一個一個點
    def shortestBridge(self, grid: List[List[int]]) -> int:
        print("DFS to find island2 ; BFS starting with the whole island2")
        if not grid or not grid[0]:
            return 0        
        m, n = len(grid), len(grid[0])
        
        # convert the first island to "2" (island2); the second island stays as "1" 
        def convertFirstIsland(grid):
            island2 = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        _dfsChange(grid, island2, i, j)
                        return island2 
            return None #no island 
                        
        def _dfsChange(grid, island2, i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid[i][j] != 1: # 0 or 2
                return 
            grid[i][j] = 2
            island2.append((i, j))
            for ni, nj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                _dfsChange(grid, island2, ni, nj)
        
        def findMinDistanceByForLoop(grid, island2):
            visited = set(island2)
            deq = collections.deque(island2)
            distance = 0
            while deq:
                for _ in range(len(deq)):
                    i, j = deq.popleft()
                    if grid[i][j] == 1:  #found island1
                        return distance - 1
                    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        if (ni, nj) in visited:
                            continue
                        deq.append((ni, nj))
                        visited.add((ni, nj))
                distance += 1
            return None  #only 1 island 
        
        def findMinDistanceByDict(grid, island2):
            deq = collections.deque(island2)
            distance = {key:0 for key in island2}
            
            while deq:
                i, j = deq.popleft()
                if grid[i][j] == 1:  #found island1
                    return distance[(i, j)] - 1
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if (ni, nj) in distance:
                        continue
                    deq.append((ni, nj))
                    distance[(ni, nj)] = distance[(i, j)] + 1
            return None  #only 1 island 
        
        #Main function 
        island2 = convertFirstIsland(grid)
        
        assert island2, "no island is found" 
        #distance = findMinDistanceByForLoop(grid, island2)
        distance = findMinDistanceByDict(grid, island2)
        
        assert distance, "only 1 island is found"
        return distance
        
    # =============================================================
    
    # DFS to chagne island1 ; BFS to find min path to island2 [5%]
    def shortestBridge1(self, grid: List[List[int]]) -> int:
        print("1")
        if not grid or not grid[0]:
            return 0
        self.minFlip = float('inf')
        
        self.printGrid(grid, "original")
        self.convertFirstIsland(grid)
        
        self.printGrid(grid, "converted")
        self.findMinFromFirstIsland(grid)
        
        return self.minFlip
    
    def convertFirstIsland(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self._dfsConvert(grid, i, j) #change to (2)
                    return 
                
    def _dfsConvert(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n:
            if grid[i][j] == 1:
                grid[i][j] = 2
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    self._dfsConvert(grid, ni, nj)
                    
    def findMinFromFirstIsland(self, grid):
        m, n = len(grid), len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    minDis = float('inf')
                    for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        minDis = min(minDis, self._bfsFind(grid, ni, nj)) #find island2 (1)
                    minDis = min(minDis, self._bfsFind(grid, i, j)) #find island2 (1)

                    self.minFlip = min(self.minFlip, minDis)
                    
    # OK
    def _bfsFind(self, grid, row, col):
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
            
    # DFS (Failed)
    def _dfsFind(self, grid, i, j, distance, dis):
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
                    self._dfsFind(grid, ni, nj, distance, dis)
                #grid[i][j] = 0 #backtracking 

            if grid[i][j] == 1: #island-2
                self.minFlip = min(self.minFlip, distance)
                return 
            
    def printGrid(self, grid, msg):
        if not DEBUG:
            return 
        print("-----" + msg + "-----")
        for row in grid:
            print(row)
            
                