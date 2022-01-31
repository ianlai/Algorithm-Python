class Solution:
    
    #Record index lists; two loops to calculate the min distance [O(n^2): 98%]
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        wordIndexList1 = []
        wordIndexList2 = []
        for idx, word in enumerate(wordsDict):
            if word == word1:
                wordIndexList1.append(idx)
            if word == word2:
                wordIndexList2.append(idx)
        res = inf
        for i in wordIndexList1:
            for j in wordIndexList2:
                res = min(res, abs(i-j))
        return res