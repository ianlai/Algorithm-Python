
# Trie [89%]
class Node:
    def __init__(self):
        self.chmap = collections.defaultdict(Node)
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.chmap[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        print("search:", word)
        root = self.root
        return self.searchFromNode(word, root, 0)
    
    def searchFromNode(self, word, node, idx) -> bool:
        #print("  searchFN:", word, "node:", node.chmap.keys(), idx)

        c = word[idx]  #won't let idx over word so we don't need to check
        if c == ".":
            if len(node.chmap) == 0:  #no more chars to match
                return False
            for _, n in node.chmap.items(): 
                if idx == len(word) - 1:
                    if n.isEnd:
                        return True
                else:
                    if self.searchFromNode(word, n, idx+1):
                        return True
            return False
        else:  #alphabet 
            n = node.chmap.get(c, None)
            if n:
                if idx == len(word) - 1:
                    return n.isEnd 
                else:
                    return self.searchFromNode(word, n, idx+1)
            else:
                return False
            

    # Works, but the code is messy 
    def searchFromNode1(self, word, node, idx) -> bool:
        #print("  searchFN:", word, "node:", node.chmap.keys(), idx)

        if idx == len(word) - 1:
            c = word[idx]
            if c == ".":
                for _, n in node.chmap.items():
                    if n.isEnd is True:
                        return True
                return False
                
            n = node.chmap.get(c, None)
            if n:
                return n.isEnd
            else:
                return False
        
        c = word[idx]
        if c == ".":
            if len(node.chmap) == 0:
                return False
            for _, n in node.chmap.items():
                if self.searchFromNode(word, n, idx+1):
                    return True
            return False
        else:
            if c in node.chmap:
                n = node.chmap.get(c)
                return self.searchFromNode(word, n, idx+1)
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)