'''
Autocomplete

給一堆字串，再給一個目標字串，回傳開頭和目標字串相同的字串list。

Leetcode的輸出最多三個，且需要Sorted過。
不需要Sort的話Trie就可以全取。

(1) Trie + DFS  
(2) Sorting + Binary Search
'''


'''
(1) Trie + DFS 

T.C. = O(NL + L)   #L是字長
S.C. = O(NL)

'''
from bisect import bisect_left

class Node:
    def __init__(self):
        self.chmap = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):  #
        cur = self.root
        for c in word:
            if c not in cur.chmap:
                cur.chmap[c] = Node()
            cur = cur.chmap[c]
        cur.isEnd = True

    def search(self, word):     #return words[]
        cur = self.root
        for c in word:
            if c not in cur.chmap:
                return []
            cur = cur.chmap[c]

        # Return word + self._findWords(cur)
        return [word + "".join(string) for string in self._findWords(cur)]

    def _findWords(self, root):
        res = []
        self._dfs(root, res, [])
        return res
    
    def _dfs(self, node, res, path):
        if node.isEnd:
            res.append(list(path))
        for c, nxt in node.chmap.items():
            self._dfs(nxt, res, path + [c])

wordList = ["bags", "bag", "bagger", "box", "boxer", "bam", "bammer", "bit", "cat", "can", "bitty"]
target = "c"

def findSuggestionsWithTrie(wordList, target):
    trie = Trie()
    for word in wordList:
        trie.add(word)
    return trie.search(target)

print("Trie:", findSuggestionsWithTrie(wordList, target))



'''
(2) Sorting + Binary Search

T.C. = O(NlogN ~ N2 + logN + T)   Targetword length: T 
S.C. = O(logN ~ N)
'''
def findSuggestionsWithBS(wordList, target):
    wordList.sort()
    #print(sortedList)
    idx = bisect_left(wordList, target)
    res = []
    targetLength = len(target)
    for i in range(idx, len(wordList)):
        if wordList[i][:targetLength] != target:
            break
        else:
            res.append(wordList[i])
    return res
print("BS:", findSuggestionsWithBS(wordList, target))
