class WordDistance:
    
    # 2022/01/31
    # Use map to store indices of each word
    # Use two loops to find min distances of the two word map [O(n2): 48%]
    
    # O(n) 
    def __init__(self, wordsDict: List[str]):
        self.wordToIndexList = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.wordToIndexList[word].append(idx)

    # 2022/02/15
    # Two-Pointer [O(n): 59%]
    def shortest2(self, word1: str, word2: str) -> int:       
        #print("Code2")
        i1 = i2 = 0
        w1 = self.wordToIndexList[word1]
        w2 = self.wordToIndexList[word2]
        #print(w1, w2)
        minDiff = inf
        
        ### 同向雙指標 Two pointer 
        while i1 < len(w1) and i2 < len(w2):
            minDiff = min(minDiff, abs(w1[i1] - w2[i2]))
            if w1[i1] < w2[i2]:
                i1 += 1 
            else:
                i2 += 1
                
        ### Sliding window (Incorrect)
        # for i1, v1 in enumerate(w1):
        #     while i2 < len(w2) and w2[i2] < v1:
        #         minDiff = min(minDiff, abs(v1 - w2[i2]))
        #         i2 += 1
        #     minDiff = min(minDiff, abs(v1 - w2[-1]))
            
        return minDiff
    
    # Two loop [O(n2): 41%] 
    def shortest(self, word1: str, word2: str) -> int:       
        #print("Code1")
        res = inf
        for i in self.wordToIndexList[word1]:
            for j in self.wordToIndexList[word2]:
                res = min(res, abs(i-j))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)