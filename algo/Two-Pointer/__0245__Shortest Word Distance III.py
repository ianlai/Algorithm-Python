class Solution:
    
    # Two Pointer [O(n): 70% / O(n): 75%]
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
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