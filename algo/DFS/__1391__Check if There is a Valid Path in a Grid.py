class Solution:
    
    # 2022/05/06
    # DFS (not backtracking) [O(MN): 90% / O(MN): 30%]
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        print("Code3")
        m, n = len(grid), len(grid[0])
        sToDir = {
            1: [1, 3],
            2: [0, 2],
            3: [2, 3],
            4: [1, 2],
            5: [0, 3],
            6: [0, 1]
        }
        dirToS = {
            0: {2, 3, 4},
            1: {1, 3, 5},
            2: {2, 5, 6},
            3: {1, 4, 6}
        }
        nextDir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def dfs(x, y, visited):
            if x == m - 1 and y == n - 1:
                return True
            for d in sToDir[grid[x][y]]:
                nx, ny = x + nextDir[d][0], y + nextDir[d][1]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] not in dirToS[d]:
                    continue
                if visited[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                if dfs(nx, ny, visited):
                    return True
            return False
                
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1
        return dfs(0, 0, visited) 
        
        
    # 2021/06/29 
    # DFS (backtracking)  [45% / 27%]  //後來再看感覺backtracking不需要
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        print("Code2: DRY code")
        if not grid or not grid[0]:
            return True
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        self.grid = grid
        self.nToD = {
            1: ["r", "l"],
            2: ["u", "d"],
            3: ["l", "d"],
            4: ["r", "d"], 
            5: ["l", "u"],
            6: ["u", "r"]
        }
        # self.dToC = {  #direction to Current
        #     "r": [1, 4, 6], 
        #     "d": [2, 3, 4],
        #     "l": [1, 3, 5],
        #     "u": [2, 5, 6]
        # }
        self.dToN = {  #direction to Next
            "r": [1, 3, 5], 
            "d": [2, 5, 6],
            "l": [1, 4, 6],
            "u": [2, 3, 4]
        }
        self.dToS = {
            "r": [ 0, 1],  
            "d": [ 1, 0],
            "l": [ 0,-1],
            "u": [-1, 0]
        }
        visited = [[0 for _ in range(n)] for _ in range(m)]
        return self.dfs(0, 0, visited)
    
    def dfs(self, i, j, visited):
        #print(i, j)
        m, n = len(self.grid), len(self.grid[0])

        for d in self.nToD[self.grid[i][j]]:
            #print(i, j, "->", d )
            ni = i + self.dToS[d][0]
            nj = j + self.dToS[d][1]
            
            if not (0 <= ni < m and 0 <= nj < n) :
                #print(i, j, "->", d , "out")
                continue

            tMap = self.dToN[d]
            if self.grid[ni][nj] not in tMap:
                #print(i, j, "->", d , "no")
                continue
            if visited[ni][nj] == 1:
                #print(i, j, "->", d , "visited")
                continue
                
            if ni == m - 1 and nj == n - 1:
                return True
            
            visited[ni][nj] = 1
            if self.dfs(ni, nj, visited):
                return True
            visited[ni][nj] = 0
        return False
        
        # ======================================
        
    def hasValidPath1(self, grid: List[List[int]]) -> bool:
        print("Not so DRY code")
        if not grid or not grid[0]:
            return True
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        self.grid = grid        
        self.tr = {
            1: [1, 3, 5], 
            2: [],
            3: [],
            4: [1, 3, 5], 
            5: [],
            6: [1, 3, 5]
        }
        self.tl = {
            1: [1, 4, 6], 
            2: [],
            3: [1, 4, 6],
            4: [], 
            5: [1, 4, 6],
            6: []
        }
        self.td = {
            1: [], 
            2: [2, 5, 6],
            3: [2, 5, 6],
            4: [2, 5, 6], 
            5: [],
            6: [] 
        }
        self.tu = {
            1: [], 
            2: [2, 3, 4],
            3: [],
            4: [], 
            5: [2, 3, 4],
            6: [2, 3, 4]
        }
        self.dToT = {
            "r": self.tr,
            "d": self.td,
            "l": self.tl,
            "u": self.tu
        }
        self.dToS = {
            "r": [ 0, 1],  
            "d": [ 1, 0],
            "l": [ 0,-1],
            "u": [-1, 0]
        }
        visited = [[0 for _ in range(n)] for _ in range(m)]
        return self.dfs1(0, 0, visited)
    
    def dfs1(self, i, j, visited):
        #print(i, j)
        m, n = len(self.grid), len(self.grid[0])
        
        for d in ["r", "d", "l", "u"]:
            #print(i, j, "->", d )
            ni = i + self.dToS[d][0]
            nj = j + self.dToS[d][1]
            
            if not (0 <= ni < m and 0 <= nj < n) :
                #print(i, j, "->", d , "out")
                continue
            
            tMap = self.dToT[d]
            if self.grid[ni][nj] not in tMap[self.grid[i][j]]:

                #print(i, j, "->", d , "no")
                continue
            if visited[ni][nj] == 1:
                #print(i, j, "->", d , "visited")
                continue
                
            if ni == m - 1 and nj == n - 1:
                return True
            
            visited[ni][nj] = 1
            if self.dfs1(ni, nj, visited):
                return True
            visited[ni][nj] = 0
            
        return False