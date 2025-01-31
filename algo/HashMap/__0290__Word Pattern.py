class Solution:
    
    # O(n*L), 94%
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not s or not pattern:
            return False
        strArr = s.split()
        pToS = {}
        strSet = set()
        
        if len(strArr) != len(pattern):  #len different 
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in pToS:
                if pToS[pattern[i]] != strArr[i]:  #pattern maps to different word
                    return False
            else:
                if strArr[i] in strSet:  #same word maps to different patterns
                    return False
                pToS[pattern[i]] = strArr[i]
                strSet.add(strArr[i])
                
        return True