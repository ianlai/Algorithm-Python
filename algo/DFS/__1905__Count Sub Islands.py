class Solution:
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
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
                    self.dfs(grid1, grid2, i, j, 0, visited)
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
                self.dfs(grid1, grid2, i, j, 0, visited)
                count += 1
        return count
    
    def dfs(self, grid1, grid2, i, j, setTo, visited):
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
            self.dfs(grid1, grid2, ni, nj, setTo, visited)
            
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
        