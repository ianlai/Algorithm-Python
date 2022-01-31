class WordDistance:

    
    # 2022/01/31
    # Use map to store indices of each word
    # Use two loops to find min distances of the two word map [O(n2): 48%]
    
    # O(n) 
    def __init__(self, wordsDict: List[str]):
        self.wordToIndexList = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.wordToIndexList[word].append(idx)

    # O(n2)
    def shortest(self, word1: str, word2: str) -> int:
        res = inf
        for i in self.wordToIndexList[word1]:
            for j in self.wordToIndexList[word2]:
                res = min(res, abs(i-j))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)