class Solution:
    
    
    #O(S+T): 5%
    def isSubsequence(self, s: str, t: str) -> bool:
        print("Code2")
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
    
    # Incorrect
    def isSubsequence1(self, s: str, t: str) -> bool:
        print("Code1")
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        ti = 0
        for si, sch in enumerate(s):
            while ti < len(t):
                if sch == t[ti]:
                    ti += 1
                    if ti == len(t):
                        if si == len(s):
                            return True
                        else:
                            return False
                    break
                else:
                    ti += 1
        return False
                