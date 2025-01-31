class Solution:
    
    # String handling [O(s+t): 40%]
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
        else:
            if len(s) < len(t):  
                s, t = t, s  #let s be longer 
            for i in range(len(s)):
                if i == len(t):
                    return True
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
        return False