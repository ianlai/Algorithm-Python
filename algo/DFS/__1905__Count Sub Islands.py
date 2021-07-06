class Solution:
    
    
    # Use isSubIsland var to record the status + DFS [O(mn): 66%]
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("2021/07/06")
        def dfs(i, j):
            for ni, nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if visited[ni][nj] == 1:
                    continue
                if grid2[ni][nj] == 0:
                    continue
                if grid1[ni][nj] == 0:
                    self.isSubIsland = False    
                visited[ni][nj] = 1
                dfs(ni, nj)
                
        if not grid1 or not grid1[0]:
            return 0
        
        m, n = len(grid1), len(grid1[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and visited[i][j] == 0:
                    self.isSubIsland = True
                    
                    if grid1[i][j] == 0:   # if first point leads to a non-island
                        self.isSubIsland = False
                        
                    dfs(i, j)              # if any later point leads to a non-island
                        
                    if self.isSubIsland:
                        count += 1
        return count
    
    # =====================================================
    
    # Two Steps DFS/BFS [O(mn): 55%]
    # Step1: Change non-subislands to water
    # Step2: Count subislands 
    # Not using visited 
    def countSubIslands1(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Two steps")
        if not grid1 or not grid1[0]:
            return 0
        
        m, n = len(grid1), len(grid1[0])
        
        print("==== grid1 ====")
        for row in range(m):
            print(grid1[row])
        print("==== grid2 ====")
        for row in range(m):
            print(grid2[row])
            
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        # Step1: Clean the non-subisland in grid2
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0: #not sub island
                    print("Found non-subisland:", i, j)
                    #self.dfs(grid1, grid2, i, j, 0)
                    self.bfs(grid1, grid2, i, j, 0)
                    continue
        print("==== grid2 (after processed) ====")
        
        # Step2: Count the remaining islands in grid2 
        count = 0
        for row in range(m):
            print(grid2[row])
            
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 0:
                    continue
                #self.dfs(grid1, grid2, i, j, 0)
                self.bfs(grid1, grid2, i, j, 0)
                count += 1
        return count
    
    def bfs(self, grid1, grid2, i, j, setTo):
        m, n = len(grid1), len(grid1[0])
        queue = collections.deque([(i, j)])
        while queue:
            #(x, y) = queue.popleft()  #BFS
            (x, y) = queue.pop()  #DFS
            grid2[x][y] = setTo
            for (nx, ny) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                #if 0 <= nx < m and 0 <= ny < n 
                if grid2[nx][ny] == 1:
                    #grid2[nx][ny] = setTo
                    queue.append((nx, ny))
    
    def dfs(self, grid1, grid2, i, j, setTo):
        m, n = len(grid1), len(grid1[0])
        
        #print("  i,j = ", i, j)    
        
        if not (0 <= i < m and 0 <= j < n):
            return False
        
        if grid2[i][j] == 0:
            return False
        
        grid2[i][j] = setTo
        
        for di, dj in [(0, 1), (0, -1,), (1, 0), (-1, 0)]:
            ni = i + di
            nj = j + dj
            self.dfs(grid1, grid2, ni, nj, setTo)
            
        return True
    
    # ================================
    
    # Big Bro [INCORRECT]
    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid1[0]:
            return 0
        
        m, n = len(grid1), len(grid1[0])
        print("==== grid1 ====")
        for row in range(m):
            print(grid1[row])
        print("==== grid2 ====")
        for row in range(m):
            print(grid2[row])
            
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        count = 0
        for i in range(m):
            for j in range(n):
                
                if visited[i][j] == 1:
                    continue
                    
                if grid2[i][j] == 0:
                    continue
                    
                #if grid2[i][j] == 1 and grid1[i][j] == 0:
                #    continue

                print("i,j = ", i, j)    
                if self.dfs2(grid1, grid2, i, j, visited):
                    print("ok")
                    count += 1
                else:
                    print("nok")
                
        return count
    
    def dfs2(self, grid1, grid2, i, j, visited):
        m, n = len(grid1), len(grid1[0])
        
        print("  i,j = ", i, j)    
        if i == 9 and j == 0:
            for row in visited:
                print(row)
        
        if not (0 <= i < m and 0 <= j < n):
            return True
        
        if grid2[i][j] == 1 and grid1[i][j] == 0:  #not subisland
            return False
        
        if visited[i][j] == 1:
            return True
	
        visited[i][j] = 1
        
        if grid2[i][j] == 0: 
            return True
        
        if grid2[i][j] == 1 and grid1[i][j] == 0:  #not subisland
            return False
        
        for di, dj in [(0, 1), (0, -1,), (1, 0), (-1, 0)]:
            ni = i + di
            nj = j + dj
                
            if not self.dfs2(grid1, grid2, ni, nj, visited):
                return False
        return True
        
    # ===================================
        
#     def dfs(self, grid1, grid2, i, j, visited):
#         m, n = len(grid1), len(grid1[0])
        
#         print("  i,j = ", i, j)    
#         # if i == 9 and j == 0:
#         #     for row in visited:
#         #         print(row)
        
#         if not (0 <= i < m and 0 <= j < n):
#             return True
        
#         if visited[i][j] == 1:
#             return True
	
#         visited[i][j] = 1
        
#         if grid2[i][j] == 0: 
#             return True
        
#         if grid2[i][j] == 1 and grid1[i][j] == 0:  #not subisland
#             return False
        
#         for di, dj in [(0, 1), (0, -1,), (1, 0), (-1, 0)]:
#             ni = i + di
#             nj = j + dj
            
# #             if not (0 <= ni < m and 0 <= nj < n):
# #                 continue
                
# #             if visited[ni][nj] == 1:
# #                 continue
# #                 #return False
            
# #             if grid2[ni][nj] == 1 and grid1[ni][nj] == 0:
# #                 return False
                
# #             visited[ni][nj] = 1
            
# #             if grid2[ni][nj] == 0 and grid1[ni][nj] == 0:
# #                 continue
                
# #             if grid2[ni][nj] == 0 and grid1[ni][nj] == 1:
# #                 continue
                
#         #     if not self.dfs(grid1, grid2, ni, nj, visited):
#         #         return False
#         # return True
        