'''
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],  
    ['c', 'c', 'a', 't', 'n', 't'],  
    ['a', 'c', 'n', 'n', 't', 't'],  
    ['t', 'n', 'i', 'i', 'p', 'p'],  
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "ant"
word5 = "aoi"
word6 = "ki"
word7 = "aaoo"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
find_word_location(grid1, word3) => [(5, 0)]
find_word_location(grid1, word4) => [(0, 4), (1, 4), (2, 4)] OR [(0, 4), (1, 4), (1, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 2), (5, 3), (5, 4), (5, 5)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word
'''

words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"

grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],  
    ['c', 'c', 'a', 't', 'n', 't'],  
    ['a', 'c', 'n', 'n', 't', 't'],  
    ['t', 'n', 'i', 'i', 'p', 'p'],  
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "ant"
word5 = "aoi"
word6 = "ki"
word7 = "aaoo"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

# TC: O(WS + SWS) = O(WS^2)
# SC: O(W*26)  
import collections
def find_embedded_word(words, target):
    wordCount = collections.defaultdict(lambda: collections.defaultdict(int))
    for word in words:
        for ch in word:
            wordCount[word][ch] += 1
    #print(wordCount)
    
    targetCount = collections.defaultdict(int)
    for ch in target:
        targetCount[ch] += 1
        # compare 
        for word, wordMap in wordCount.items():
            isValid = True
            for c, count in wordMap.items():
                #print(c, count, targetCount)
                if count > targetCount[c]:
                    isValid = False
                    break
            if isValid: 
                return word
        #print(targetCount)
    return None
    
# print(find_embedded_word(words, string1))
# print(find_embedded_word(words, string2))
# print(find_embedded_word(words, string3))
# print(find_embedded_word(words, string4))
# print(find_embedded_word(words, string5))
# print(find_embedded_word(words, string6))


# TC: O(rc * 2^w) 
# SC: O(w + w) = O(w) 
def dfs(grid, i, j, cur, idx, word, res):
    m, n = len(grid), len(grid[0])
    if idx == len(word):
        res.append(list(cur))
        return True
    if not (0 <= i < m and 0 <= j < n):
        return False
    if grid[i][j] != word[idx]:
        return False
    cur.append((i, j))
    for (ni, nj) in [(i+1, j), (i, j+1)]:
        if dfs(grid, ni, nj, cur, idx+1, word, res):
            return True
    cur.remove((i, j))

def find_word_location(grid, word):
    m, n = len(grid), len(grid[0])
    res = []
    for i in range(m):
        for j in range(n):
            #cur = [(i, j)]
            cur = []
            if dfs(grid, i, j, cur, 0, word, res):
                return res[0]
    return []

print(find_word_location(grid1, word1))
print(find_word_location(grid1, word2))
print(find_word_location(grid1, word3))
print(find_word_location(grid1, word4))
print(find_word_location(grid1, word5))
print(find_word_location(grid1, word6))
print(find_word_location(grid1, word7))
print(find_word_location(grid1, word8))
print(find_word_location(grid2, word9))

'''
find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
find_word_location(grid1, word3) => [(5, 0)]
find_word_location(grid1, word4) => [(0, 4), (1, 4), (2, 4)] OR [(0, 4), (1, 4), (1, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 2), (5, 3), (5, 4), (5, 5)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]
'''