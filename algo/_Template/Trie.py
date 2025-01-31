# dictionary: N (words)
# length    : L 
# sentence  : S (words) 大


# Approach1: 每個字掃
#  TC : O(NL * S)
#  SC : O(1)

# Approach2: Prefix Set
#  TC : O(L^2 * N + L * S )  (build, find)
#  SC : O(L^2 * N)

# Approach3: Prefix Tree
#  TC : O(L * N + L * S)     (build, find)
#  SC : O(L * N)

'''
Approach1，沒有預處理，找的速度慢。
Approach2，使用Prefix Set做預處理，使用了空間來換時間。
Approach3，使用Trie來做預處理，比Prefix Set不佔空間，且預處理的時間也較短，而且找的速度還是一樣快的
'''

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
                return word[:i+1] #found a prefix 
