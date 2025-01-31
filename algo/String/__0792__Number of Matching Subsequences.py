class Solution:
    
    # 2022/02/12
    # Aggregate the strings to 26 char buckets
    # copy bucket beforehand + string index [O(S+L*N): 58%]
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        print("Code6")
        buckets = [[] for _ in range(26)]
        for word in words:
            idx = ord(word[0]) - ord('a')
            buckets[idx].append((word, 0))

        res = 0
        for sch in s:
            idx = ord(sch) - ord('a')
            oldBucket = buckets[idx]
            buckets[idx] = []
            
            for word, position in oldBucket:
                next_position = position + 1
                if next_position == len(word):
                    res += 1
                else:
                    idx = ord(word[next_position]) - ord('a')
                    buckets[idx].append((word, next_position))
        return res
    
    # ==============================================================

    #2022/02/11
    # Aggregate the strings to 26 char buckets
    # copy bucket beforehand + string slicing [O(S+L2*N): 39%]
    def numMatchingSubseq5(self, s: str, words: List[str]) -> int:
        print("Code5")
        buckets = [[] for _ in range(26)]
        for word in words:
            idx = ord(word[0]) - ord('a')
            buckets[idx].append(word)
        #print(buckets)

        res = 0
        for si in range(len(s)):
            sch = s[si] 
            sidx = ord(sch) - ord('a')
            oldBucket = buckets[sidx]
            buckets[sidx] = []
            for word in oldBucket:
                if len(word) == 1:
                    res += 1
                else:
                    idx = ord(word[1]) - ord('a')
                    buckets[idx].append(word[1:])
        return res
    # ==============================================================
    #2022/02/11
    # Aggregate the strings to 26 char buckets; handle temp bucket [O(S+L*N): 35%]
    def numMatchingSubseq4(self, s: str, words: List[str]) -> int:
        print("Code4")
        buckets = [[] for _ in range(26)]
        for word in words:
            idx = ord(word[0]) - ord('a')
            buckets[idx].append(word)
        #print(buckets)

        res = 0
        for si in range(len(s)):
            sch = s[si] 
            sidx = ord(sch) - ord('a')
            #print(buckets[sidx])
            temp = []
            for word in buckets[sidx]:
                if len(word) == 1:
                    res += 1
                else:
                    idx = ord(word[1]) - ord('a')
                    if idx != sidx:
                        buckets[idx].append(word[1:])
                    else:
                        temp.append(word[1:])
            buckets[sidx] = temp 
        return res
    # ==============================================================
    # Scan s only once but every word will not end even if completed [O(S*N): TLE]
    def numMatchingSubseq3(self, s: str, words: List[str]) -> int:
        print("Code3")
        count = 0
        si = 0
        wordIndices = [0] * len(words)
        while True:
            for i, wordIndex in enumerate(wordIndices):
                if wordIndices[i] == -1:
                    continue
                if words[i][wordIndex] == s[si]:
                    wordIndices[i] += 1
                if wordIndices[i] == len(words[i]):
                    wordIndices[i] = -1
                    count += 1
                    continue
            si += 1
            if si == len(s):
                break            
        return count
    
    # ==============================================================
    # TLE
    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        print("Code2")
        def isSubsequence(s, w):
            if len(w) == 0:
                return True
            if len(s) == 0:
                return False
            if s[0] == w[0]:
                return isSubsequence(s[1:], w[1:])
            return isSubsequence(s[1:], w)
            
        count = 0
        for word in words:
            if isSubsequence(s, word):
                count += 1
        return count
    
    
    # ==============================================================
    # TLE
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        print("Code1")
        def isSubsequence(s, word):
            si = wi = 0
            while True:
                if s[si] == word[wi]:
                    wi += 1
                    si += 1
                if wi == len(word):
                    return True
                if si == len(s) and wi != len(word):
                    return False

                
            # for i, ch in enumerate(word):
            #     while idx < len(s):
            #         if s[idx] == ch:
            #             idx += 1    
            #     if idx == len(s) and i != len(word):
            #         return False
            # return True
            
        count = 0
        for word in words:
            if isSubsequence(s, word):
                count += 1
        return count
            