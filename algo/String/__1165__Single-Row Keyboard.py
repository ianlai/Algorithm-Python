class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if len(word) == 0:
            return 0
        
        chToIdx = {}
        for i, ch in enumerate(keyboard):
            chToIdx[ch] = i
        
        steps = chToIdx[word[0]]
        for i in range(1, len(word)):
            steps += abs(chToIdx[word[i]] - chToIdx[word[i-1]])
            
        return steps