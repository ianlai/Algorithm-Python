class Node():
    def __init__(self, ch = ""):
        self.char = ch
        self.charmap = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for ch in word:
            if ch in cur.charmap:
                cur = cur.charmap[ch]
            else:
                nextNode = Node(ch)
                cur.charmap[ch] = nextNode
                cur = nextNode
        cur.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.charmap:
                return False
            cur = cur.charmap[ch]
        # if len(cur.charmap) != 0:
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.charmap:
                return False
            cur = cur.charmap[ch]
        return True
        
class Solution:
    
    # DFS + Trie [TLE]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("Tries")
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        
        m = len(board)
        n = len(board[0])
        #prefixSet = set("")
        #wordSet = set()
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        results = set()  #remove redundancies 
        
        #create Tries
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # for word in words:
        #     wordSet.add(word)
        
        for i in range(m):
            for j in range(n):
                #print(board[i][j])
                visited[i][j] = 1
                self.dfs3(board, words, trie, i, j, board[i][j], visited, results) #cur starts with board[i][j]
                visited[i][j] = 0  #backtracking 
        return list(results)
    
    def dfs3(self, board, words, trie, i, j, cur, visited, results):
        curStr = "".join(cur)
        
        #if curStr not in prefixSet:
        #    return 
        if not trie.startsWith(curStr):
            return 
    
        # if curStr in wordSet: 
        #     results.add(curStr)
            # keep searching
        if trie.search(curStr):
            results.add(curStr)
            
        m = len(board)
        n = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # next 
        for d in dirs:
            nextI = i + d[0]
            nextJ = j + d[1]
            
            # current
            if not (0 <= nextI < m and 0 <= nextJ < n): #check the board 
                continue
            if visited[nextI][nextJ] == 1: #remove the redundancies
                continue        
            
            visited[nextI][nextJ] = 1
            nextWord = board[nextI][nextJ]
            #print(">>> ", nextI, nextJ, cur + nextWord)
            self.dfs3(board, words, trie, nextI, nextJ, cur + nextWord, visited, results)  #concatanate the cur string 
            visited[nextI][nextJ] = 0         # backtracking


            
    # ===========================================
    # DFS + PrefixSet [O(MN * 3^L * 1? : 21%]  //Boardsize: M * N ; WordList: T words with max L size
    # Note: Don't use list and add unnecessary conversation between list and string
    # Note: Use set instead of list
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("PrefixSet")
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
        #print("prefixSet:", prefixSet)
        #print("wordSet:", wordSet)
        
        for i in range(m):
            for j in range(n):
                self.dfs2(board, prefixSet, wordSet, i, j, board[i][j], visited, res) #cur starts with board[i][j]
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