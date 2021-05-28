DIR = [(0,1), (0,-1), (1,0), (-1,0)]

class Solution:
    
    # DFS [O(n^2 * 3^L * 1), 5%]
    # - Compare one char by one char on the fly.
    # - Not need to store the PrefixSet 
    # - Not need to store the cur list. 
    # - i, j: the coordinates for board
    # - idx : the coordinates for word
    def exist(self, board: List[List[str]], word: str) -> bool:
        print("Compare on the fly")
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