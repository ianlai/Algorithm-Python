class Solution:
    
    # 2022/06/05
    # Two Pointer [O(n): 46% / O(1): 29%]
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print("Code2")
        idx1, idx2 = -1, -1
        minDistance = inf
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx1 = i
                if idx2 != -1:
                    minDistance = min(minDistance, abs(idx1 - idx2))
            if wordsDict[i] == word2:
                idx2 = i
                if idx1 != -1 and idx1 != idx2:
                    minDistance = min(minDistance, abs(idx1 - idx2))
        return minDistance
    
    # 2022/05/02
    # Two Pointer [O(n): 70% / O(n): 75%]
    def shortestWordDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print("Code1")
        if word1 == word2:
            wlist = []
            for i, w in enumerate(wordsDict):
                if w == word1:
                    wlist.append(i)
            minDistance = inf
            for i in range(1, len(wlist)):
                minDistance = min(minDistance, wlist[i] - wlist[i-1])
            return minDistance
                
        else:
            wlist1, wlist2 = [], []
            for i, w in enumerate(wordsDict):
                if w == word1:
                    wlist1.append(i)
                elif w == word2:
                    wlist2.append(i)
            
            i = j = 0
            minDistance = inf
            while i < len(wlist1) and j < len(wlist2):
                if wlist1[i] < wlist2[j]:
                    minDistance = min(minDistance, wlist2[j] - wlist1[i])
                    i += 1
                else:
                    minDistance = min(minDistance, wlist1[i] - wlist2[j])
                    j += 1
            while j < len(wlist2):
                minDistance = min(minDistance, abs(wlist1[i-1] - wlist2[j]))
                j += 1
            while i < len(wlist1):
                minDistance = min(minDistance, abs(wlist2[j-1] - wlist1[i])) 
                i += 1 
            return minDistance