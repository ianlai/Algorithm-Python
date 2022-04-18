class Node():
    
    # not need to store char 
    def __init__(self):
        self.charmap = {}
        self.isEnd = False
        
        #store the word at the leaf for easier getting the whole word
        self.word = "" 

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.charmap:
                cur.charmap[c] = Node()
            cur = cur.charmap[c] 
        cur.isEnd = True
        cur.word = word
        
    # def search(self, word: str) -> bool, bool:
    #     cur = self.root
    #     for c in word:
    #         if c not in cur.charmap:
    #             return False, None
    #         cur = cur.charmap[c]
    #     return True, cur.isEnd     
        
class Solution:
    
    # 2022/04/18
    # DFS + Trie (search function not needed) [Time: O(N*4*3^(L-1)): 57% / Space: O(WL): 5%]
    # Prune the node without valid children
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("Code3: Tries")
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        m, n  = len(board), len(board[0])
        
        def dfs(i, j, node, visitied, res):
            assert 0 <= i < m and 0 <= j < n
            
            if board[i][j] not in node.charmap:
                return 
            
            nextNode = node.charmap[board[i][j]]
            if nextNode.isEnd:
                res.add(nextNode.word)
                #prune
                if len(nextNode.charmap) == 0:
                    del node.charmap[board[i][j]]
            
            # if (i, j) in visited:  <---incorrect
            #     return
            visited.add((i, j))
            #visited[i][j] = 1
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if (ni, nj) in visited:
                #if visited[ni][nj] == 1:
                    continue
                dfs(ni, nj, nextNode, visited, res)
            visited.remove((i, j))
            #visited[i][j] = 0
            
        #both visited set or visited matrix got same result of speed
        visited = set()
        #visited = [[0 for _ in range(n)] for _ in range(m)] 
        res = set()  #remove redundancies 
        
        #Create Tries
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        #DFS to search
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, visited, res) #cur starts with board[i][j]
                
        return list(res)
    
    # =================================================
    # 2021/10/22
    # DFS + Trie (DFS to search) [Time: TLE~11% -> O(N*4*3^(L-1)): 63% (prune words at leaf) / ]
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("Code2: Tries")
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        
        m, n  = len(board), len(board[0])
        self.board = board
        self.words = words 
        self.visited = [[0 for _ in range(n)] for _ in range(m)] 
        self.res = set()  #remove redundancies 
        
        #Create Tries
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        
        #DFS
        for i in range(m):
            for j in range(n):
                self.dfs3(i, j, self.trie.root) #cur starts with board[i][j]
        return list(self.res)
    
    def dfs3(self, i, j, node):
        
        #Search 
        if self.board[i][j] not in node.charmap:
            return
        parent = node
        node = node.charmap[self.board[i][j]]
        if node.isEnd:
            self.res.add(node.word)
            if len(node.charmap) == 0:   #prune the found words at leaf
                del parent.charmap[self.board[i][j]]
                return
    
        #Next 
        m, n  = len(self.board), len(self.board[0])
        self.visited[i][j] = 1
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:            
            if not (0 <= ni < m and 0 <= nj < n): #check the board 
                continue
            if self.visited[ni][nj] == 1: #remove the redundancies
                continue
            self.dfs3(ni, nj, node)
                
        self.visited[i][j] = 0  # backtracking
            
            
    # ===========================================
    # 2021/10/22
    # DFS + PrefixSet [Time: O(MN*4(3^L-1)*L): 5% / Space: O(T^2*L) 93%] //Boardsize: M*N ; WordList: T words with max L size
    # Note: Don't use list and add unnecessary conversation between list and string
    # Note: Use set instead of list
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("Code1: PrefixSet")
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        
        m, n = len(board), len(board[0])
        prefixSet = set()
        wordSet = set(words)
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        res = set()  #remove redundancies 
        
        #Create prefix-set
        for word in words:
            for i in range(len(word) + 1):
                prefixSet.add(word[:i])
        #DFS
        for i in range(m):
            for j in range(n):
                self.dfs2(board, prefixSet, wordSet, i, j, board[i][j], visited, res) 
        return list(res)
    
    def dfs2(self, board, prefixSet, wordSet, i, j, cur, visited, res):
        if cur not in prefixSet:
            return 
        if cur in wordSet: 
            res.add(cur)  #Don't return, keep searching
            
        m, n = len(board), len(board[0])
        visited[i][j] = 1
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= ni < m and 0 <= nj < n): #check the board 
                continue
            if visited[ni][nj] == 1: #remove the redundancies
                continue
            nextChar = board[ni][nj]
            self.dfs2(board, prefixSet, wordSet, ni, nj, cur + nextChar, visited, res) 
        visited[i][j] = 0
            
    # ===========================================
         
    # DFS + PrefixSet, check and add in the current layer, use list as cur (TLE)
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        
        m = len(board)
        n = len(board[0])
        prefixSet = set("")
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        results = set()  #remove redundancies 
        
        #create prefixSet
        for word in words:
            for i in range(len(word) + 1):
                prefixSet.add(word[:i])
        print(prefixSet)
        
        for i in range(m):
            for j in range(n):
                self.dfs1(board, words, prefixSet, i, j, [], visited, results)
        return list(results)
    
    def dfs1(self, board, words, prefixSet, i, j, cur, visited, results):
        curStr = "".join(cur)
        if curStr not in prefixSet:
            return 
        if curStr in words: 
            results.add(curStr)
            # keep searching
        
        m = len(board)
        n = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # current
        if not (0 <= i < m and 0 <= j < n): #check the board 
            return 
        if visited[i][j] == 1: #remove the redundancies
            return 
        cur.append(board[i][j])
        #print(curStr, cur)
        
        # next 
        visited[i][j] = 1
        for d in dirs:
            nextI = i + d[0]
            nextJ = j + d[1]
            self.dfs1(board, words, prefixSet, nextI, nextJ, cur, visited, results)
        
        # backtrack 
        visited[i][j] = 0
        cur.pop()