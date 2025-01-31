class Solution:
    # 2022/05/11
    # BFS + isSubisland [O(MN): 63% / O(MN): 91%]  
    # (1) Iteration的好處: isSubisland的變數會一直擁有，不需要用AND或global來存
    # (2) Iteration的好處: 不會stackoverflow
    # (3) Iteration的好處: BFS或DFS任選
    # (4) Func後取出後處理的好處: 進入前不需要檢查，檢查點只要寫一個地方 
    #     -> 壞處是用不到也會裝入
    # (5) 修改grid2為0而不是用visited的好處: 空間複雜度雖然不變(還是有deq)但使用的空間少很多 
    #     -> 壞處是grid2會被修改
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Code5 - 取出後處理 [BEST]")
        m, n = len(grid1), len(grid1[0])
        def bfs(startx, starty):            
            deq = collections.deque([(startx, starty)])
            isSubisland = True
            while deq:
                x, y = deq.popleft()  #可以BFS也可以DFS
                #寫一個取出後處理的版本
                if not (0 <= x < m and 0 <= y < n):
                    continue
                if grid2[x][y] == 0:
                    continue
                grid2[x][y] = 0   #visited
                
                if grid1[x][y] == 0: #not subisland 
                    #還不能回，必須要繼續標記走過的grid2
                    #但因為是bfs，沒有recursion，所以此變數不用用global來存
                    # return False 
                    isSubisland = False

                for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    deq.append((nx, ny))
            return isSubisland

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and bfs(i, j): 
                    count += 1
        return count 
    
    # 2022/05/11 
    # DFS + use isSubIsland var to record the status [O(mn): 66% / O(mn): 5%]
    # isSubIsland的結果需要用AND運算來判斷是否下層有False
    # 而因為是用for的放入前處理，所以開頭進入dfs前必須要判斷grid1也為1 (用func的取出後處理就不需要)
    def countSubIslands4(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Code4 - DFS (放入前處理)  [OK]")
        def dfs(i, j):
            isSubIsland = True
            for ni, nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if visited[ni][nj] == 1:
                    continue
                visited[ni][nj] = 1
                
                if grid2[ni][nj] == 0:
                    continue
                if grid1[ni][nj] == 0:
                    isSubIsland = False
                isSubIsland &= dfs(ni, nj)
            return isSubIsland
                
        if not grid1 or not grid1[0]:
            return 0
        
        m, n = len(grid1), len(grid1[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and visited[i][j] == 0:
                    if dfs(i, j): 
                        count += 1
        return count
        
    # 2022/05/11
    # 打算把兩個grid都是1的才保留為1，然後計算這個新的grid的島數。
    # 但這是錯的，grid2的島必須要全部都被grid1蓋住才算。
    def countSubIslands3(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Code3")
        
        def bfs(grid, startx, starty):
            m, n = len(grid), len(grid[0])
            deq = collections.deque([(startx, starty)])
            while deq:
                x, y = deq.popleft()
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    grid[nx][ny] = 0
                    deq.append((nx, ny))
        
        # Change grid2 to be both True in grid1 and grid2
        m, n = len(grid1), len(grid1[0])
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 or grid2[i][j] == 0:
                    grid2[i][j] = 0
        
        # BFS in grid2
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    bfs(grid2, i, j)
                    count += 1
        return count
        
        
    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Code2")
        def dfs(i, j):
          # assert 0 <= i < m && 0 <= j < n
          # assert not visited[i][j]
            visited[i][j] = True

            result = (grid1[i][j] == 1)
            for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                if (0 <= ni < m and 0 <= nj < n and
                    grid2[ni][nj] == 1 and not visited[ni][nj]):
                    result &= dfs(ni, nj)
            return result

        if not grid1: # avoid grid1[0] exception
            return 0
        
        m, n = len(grid1), len(grid1[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if dfs(i, j):
                        count += 1
        return count
    
    # =====================================================
    
    # Two Steps DFS/BFS [O(mn): 55%]
    # Step1: Change non-subislands to water
    # Step2: Count subislands 
    # Not using visited 
    def countSubIslands1(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        print("Code1: Two steps")
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
        