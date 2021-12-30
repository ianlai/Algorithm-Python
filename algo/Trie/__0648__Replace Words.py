class Node:
    def __init__(self):
        self.chmap = collections.defaultdict(Node)
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.chmap:
                cur.chmap[c] = Node()
            cur = cur.chmap[c]
        cur.isEnd = True
        
    def search(self, word) -> str: 
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.chmap:
                return None
            cur = cur.chmap[c]
            if cur.isEnd:
                return word[:i+1]
        
class Solution:
    
    # 2021/12/30 
    # Trie [30%]
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add(word)
            
        res = []
        for word in sentence.split():
            replacement = trie.search(word)
            if replacement is None:
                res.append(word)
            else:
                res.append(replacement)
        return " ".join(res)
            