class Node:
    def __init__(self):
        self.chmap = collections.defaultdict(Node)
        self.preCount = 0
        self.endCount = 0         
        
class Trie:

    # Use two counter to record word count and prefix count [16%]
    # Not optimized because the removed word will still stay even if the count are all 0
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.chmap[c]
            cur.preCount += 1
        cur.endCount += 1
                
    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c in cur.chmap:
                cur = cur.chmap[c]
            else:
                return 0
        return cur.endCount

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c in cur.chmap:
                cur = cur.chmap[c]
            else:
                return 0
        return cur.preCount

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.chmap:
                cur = cur.chmap[c]
                cur.preCount -= 1
        cur.endCount -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)