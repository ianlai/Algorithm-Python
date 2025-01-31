DIR = [(0,1), (0,-1), (1,0), (-1,0)]

class Solution:
    
    # 2022/04/18
    # DFS, logic in for loop (inside) [Time:O(N*3^L):85% / Space:O(L):14%]
    def exist5(self, board: List[List[str]], word: str) -> bool:
        print("Code5")
        m, n = len(board), len(board[0])
        def dfs(i, j, idx, used):
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if idx+1 == len(word):
                    return True
                #word comparison
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if board[ni][nj] != word[idx+1]:
                    continue
                #used need to be put together
                if (ni, nj) in used:
                    continue
                used.add((ni, nj))
                if dfs(ni, nj, idx + 1, used):
                    return True
                used.remove((ni, nj))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    if dfs(i, j, 0, set([(i, j)])):
                        return True
        return False
    
    # ==============================================
    
    # 2022/02/07 
    # DFS, logic in dfs function (outside) [Time: O(N*3^L): 85% / Space: O(L): 14%]
    def exist(self, board: List[List[str]], word: str) -> bool:
        print("**Code4")
        m, n = len(board), len(board[0])
        def dfs(word, i, j, idx, visited):
            if idx == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n):
                return False
            if word[idx] != board[i][j]:
                return False
            if (i, j) in visited:
                return False
            visited.add((i, j))
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if dfs(word, ni, nj, idx + 1, visited):
                    return True
            visited.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j, 0, set()):
                    return True
        return False
    
    # ==============================================
        
    # 2021/10/17
    # DFS [O(MN*3^L): 53%]
    def exist3(self, board: List[List[str]], word: str) -> bool:
        print("Code3")
        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n):
                return False
            if visited[i][j]:
                return False
            if board[i][j] != word[idx]:
                return False
            visited[i][j] = True
            for (ni, nj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if dfs(ni, nj, idx+1):
                    return True
            visited[i][j] = False
            return False
            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
                
    # ==============================================
    
    # DFS [O(n^2 * 3^L * 1), 5%]
    # - Compare one char by one char on the fly.
    # - Not need to store the PrefixSet 
    # - Not need to store the cur list. 
    # - i, j: the coordinates for board
    # - idx : the coordinates for word
    def exist1(self, board: List[List[str]], word: str) -> bool:
        print("Code2: Compare on the fly")
        if not board or len(board[0]) == 0:
            return False
        if not word:
            return True
        
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        
        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word, visited):
                    return True
        return False
    
    def dfs(self, board, i, j, idx, word, visited):
        if idx >= len(word):
            return True

        # if "".join(cur) == word:    #compare in the end
        #     return True
        
        m = len(board)
        n = len(board[0])
        
        # === Check the i, j 
        if not self.inside(board, i, j, m, n):
            return False
        if visited[i][j] == 1:
            return False
        if board[i][j] != word[idx]:  #compare on the fly  
            return False
        
        # === DFS 
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited[i][j] = 1
        for d in dirs:
            nextI = i + d[0]
            nextJ = j + d[1]
            if self.dfs(board, nextI, nextJ, idx + 1, word, visited):
                return True
        visited[i][j] = 0
        return False
    
    def inside(self, board, i, j, m, n):
        if 0 <= i < m and 0 <= j < n:
            return True
        return False    
    
    # ======================================================
    
    # DFS [O(n^2 * 3^L * L), TLE]
    def exist1(self, board: List[List[str]], word: str) -> bool:
        print("Code1")
        if not board or len(board[0]) == 0:
            return False
        if not word:
            return True
        
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        #print(visited)
        for i in range(len(board)):
            print(visited[i])
                                      
        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs1(board, i, j, [], word, visited):
                    return True
        return False
    
    def dfs1(self, board, i, j, cur, word, visited):
        #print("-----")
        #print(cur)
        if len(cur) > len(word):
            return False
        curStr = "".join(cur) 
        #print(curStr, word)
        if "".join(cur) == word:
            return True
        
        if not self.inside1(board, i, j):
            return False
        if visited[i][j] == 1:
            return False
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in dirs:
            nextI = i + d[0]
            nextJ = j + d[1]
            visited[i][j] = 1
            if self.dfs1(board, nextI, nextJ, cur + [board[i][j]], word, visited):
                return True
            visited[i][j] = 0
        return False
    
    def inside1(self, board, i, j):
        m = len(board)
        n = len(board[0])
        if 0 <= i < m and 0 <= j < n:
            return True
        return False