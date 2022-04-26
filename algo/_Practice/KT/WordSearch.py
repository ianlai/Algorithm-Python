'''
======================================
[Problem-1] 在Puzzle內找一個字串

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
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

'''
======================================
[Problem-2] 在Puzzle內找多個字串

Input:  board = 
        [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
        
        words = 
        ["oath","pea","eat","rain"]

Output: ["eat","oath"]
'''
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
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if (ni, nj) in visited:
                #if visited[ni][nj] == 1:
                    continue
                dfs(ni, nj, nextNode, visited, res)
            visited.remove((i, j))
            
        #both visited set or visited matrix got same result of speed
        visited = set()
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