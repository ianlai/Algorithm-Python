class Node:
    def __init__(self, ch = ""):
        self.ch = ch
        self.chmap = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.chmap:
                cur.chmap[c] = Node(c)
            cur = cur.chmap[c]
        cur.isEnd = True
            
    def getStartWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.chmap:
                return []
            else:
                cur = cur.chmap[c]
        #print("cur:", cur.ch)
        res = self.getPostfix(cur)
        #print("res:", res)
        return [word + "".join(text) for text in res]
    
    def getPostfix(self, root) -> List[List[chr]]: 
        res = []
        #print("-----dfs-----")
        self.dfs(root, res, [])
        return res
        
    def dfs(self, root, res, cur):
        #print("root:", root)
        #print(root.ch, root.chmap, root.isEnd)
        if len(res) == 3:
            return 
        
        #if len(root.chmap) == 0:  #end
        if root.isEnd:    
            res.append(cur)
            
        for c in sorted(root.chmap.keys()):
            self.dfs(root.chmap[c], res, cur + [c])

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        resultList = []
        
        #====== Construct 
        for product in products:
            trie.insert(product)
        
        #print(trie)
        #print(trie.getStartWith("mou"))
        
        #====== Search 
        for i in range(len(searchWord)):
            word = searchWord[:i+1]
            
            result = trie.getStartWith(word)
            #print("Search word:", word, ", Result:", result)
            resultList.append(result + [])
        return resultList