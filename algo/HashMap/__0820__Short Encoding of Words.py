class Solution:
    
    # 2022/06/20 
    # Prefix Set (Suffix, HashMap) [O(WlogW + 7W): 72% / O(7W): 61%]
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda w: -len(w))  #long -> short 
        suffixSet = set()
        res = 0
        for word in words:
            if not suffixSet:
                for i in range(len(word)):
                    suffixSet.add(word[i:])
                res += len(word) + 1
                continue
            if word in suffixSet:
                continue
            for i in range(len(word)):
                suffixSet.add(word[i:])
            res += len(word) + 1
        return res
        
                
    # Brute Force [TLE]
    def minimumLengthEncoding1(self, words: List[str]) -> int:
        words.sort(key = lambda w: -len(w))  #long -> short 
        arr = []
        for word in words:
            if not arr:
                arr.append(word)
            else:
                found = False
                for a in arr:
                    for i in range(len(a)):
                        if a[i:] == word:  #found
                            found = True
                            break
                    if found:
                        break
                if not found:
                    arr.append(word)
                    
        res = len(arr)
        for w in arr:
            res += len(w) 
        return res