# 2021/10/22
class Node:
    def __init__(self):
        self.chmap = collections.defaultdict(Node)
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
        node = self.root
        for c in word:
            node = node.chmap[c] #defaultdict removes an existance check if 
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        isStartsWith, node = self._startsWith(word)
        return node.isEnd if isStartsWith else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        isStartsWith, _ = self._startsWith(prefix)
        return isStartsWith

    def _startsWith(self, prefix: str) -> (bool, Node):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            node = node.chmap.get(c) #get removes an existance check if 
            if node is None:
                return False, node
        return True, node
    
# 2021/06/03    
# class Node:
#     def __init__(self, ch = ""):
#         self.ch = ch
#         self.chmap = {}
#         self.isEnd = False

# class Trie:
    
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Node()    

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         cur = self.root
#         for c in word:
#             if c not in cur.chmap:
#                 cur.chmap[c] = Node(c)
#             cur = cur.chmap[c]
#         cur.isEnd = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         cur = self.root
#         for c in word:
#             if c in cur.chmap:
#                 cur = cur.chmap[c]
#             else:
#                 return False
#         return cur.isEnd

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         cur = self.root
#         for c in prefix:
#             if c in cur.chmap:
#                 cur = cur.chmap[c]
#             else:
#                 return False
#         return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)