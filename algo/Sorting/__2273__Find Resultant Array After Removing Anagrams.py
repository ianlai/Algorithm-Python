class Solution:
    
    # 2022/05/15
    # Sort to check anagrams [O(Nwlogw + N): 85% / O(Nw): 42%]
    def removeAnagrams(self, words: List[str]) -> List[str]:
        wordSort = [sorted(w) for w in words]
        res = [words[0]]
        for i, w in enumerate(wordSort):
            if i > 0 and w != wordSort[i-1]:
                res.append(words[i])
        return res