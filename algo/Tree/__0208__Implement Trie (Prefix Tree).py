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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)