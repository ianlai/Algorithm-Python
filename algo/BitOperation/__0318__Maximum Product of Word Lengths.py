class Solution:
    
    # 2022/05/29
    # String + Bit Manipulation (alphabet) [O(WlogW + WL + W^2*26): 46% / O(WL): 27%]
    def maxProduct(self, words: List[str]) -> int:
        def shareLetters(idx1, idx2):
            for i in range(26):
                if wordsCharMap[idx1][i] == wordsCharMap[idx2][i] == True:
                    return True
            return False
                
        words.sort(key = lambda x: -len(x))
        
        wordsCharMap = []
        for w in words:
            charMap = [False] * 26
            for ch in w:
                charMap[ord(ch) - ord('a')] = True
            wordsCharMap.append(charMap)
    
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not shareLetters(i, j):
                    cur = len(words[i]) * len(words[j])
                    if cur <= res:
                        break
                    else:
                        res = cur
        return res  