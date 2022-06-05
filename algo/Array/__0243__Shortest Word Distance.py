class Solution:

    # 2022/06/05 
    # One pass [O(N): 68%]
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print("Code2")
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
            
        
    #Record index lists; two loops to calculate the min distance [O(n^2): 98%]
    def shortestDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print("Code1")
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