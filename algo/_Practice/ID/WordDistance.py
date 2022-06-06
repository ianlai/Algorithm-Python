'''
Word Distance

(1) 給一個word arr，和兩個字串A, B，找兩者距離  //A != B
(2) 給一個word arr，和一個pair arr，找每一個pair的距離 //A != B
(3) 給一個word arr，和兩個字串A, B，找兩者距離  //A 可能 == B （那就要用不同字）
'''

'''
(1) Linear Scan 
T.C. = O(N)
S.C. = O(1) 
'''
# One pass [O(N): 68%]
def shortestDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
    idx1, idx2 = -1, -1
    distance = inf
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            idx1 = i
        if wordsDict[i] == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1:
            distance = min(distance, abs(idx1 - idx2))
    return distance

'''
(2) 先做WordToIndexList，再用同向雙指標  
T.C. = O(W + W)
S.C. = O(W) 
'''
import collections
import math
def shortestDistance2(self, wordsDict, wordPairs) -> int:       
    wordToIndexList = collections.defaultdict(list)

    for idx, word in enumerate(wordsDict):
        wordToIndexList[word].append(idx)

    for word1, word2 in wordPairs:
        i1 = i2 = 0
        w1 = wordToIndexList[word1]
        w2 = wordToIndexList[word2]

        minDiff = math.inf

        ### 同向雙指標 Two pointer 
        while i1 < len(w1) and i2 < len(w2):
            minDiff = min(minDiff, abs(w1[i1] - w2[i2]))
            if w1[i1] < w2[i2]:
                i1 += 1 
            else:
                i2 += 1

'''
(3) Linear Scan 
T.C. = O(W + W)
S.C. = O(W) 
'''
def shortestDistance3(self, wordsDict: List[str], word1: str, word2: str) -> int:
    idx1, idx2 = -1, -1
    minDistance = math.inf
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            idx1 = i
            if idx2 != -1 and idx1 != idx2:
                minDistance = min(minDistance, abs(idx1 - idx2))
        if wordsDict[i] == word2:
            idx2 = i
            if idx1 != -1 and idx1 != idx2:
                minDistance = min(minDistance, abs(idx1 - idx2))
    return minDistance

wordDict = ["practice", "makes", "perfect", "coding", "makes"]
