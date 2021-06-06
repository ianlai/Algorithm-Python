class Solution:
    
    # DP - memoization [O(m*n), 58%]
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.isMatchImpl(s, 0, p, 0, memo) 
    
    def isMatchImpl(self, s, i, p, j, memo):
        #print(i, "-", j)
        if (i, j) in memo:
            return memo[(i, j)]
            
        if len(s) == i and len(p) == j:
            memo[(i, j)] = True
            return True
        if len(s) != i and len(p) == j:
            memo[(i, j)] = False
            return False
        if len(s) == i and len(p) != j:
            for k in range(j, len(p)):
                if p[k] != "*":
                    #print("F")
                    memo[(i, j)] = False
                    return False
            memo[(i, j)] = True
            return True
        
        #if len(s) != i and len(p) != j 
        isMatchBool = None
        if p[j] == "*":
            isMatchBool = (self.isMatchImpl(s, i, p, j + 1, memo) or  # "*" matches 0 char  
                           self.isMatchImpl(s, i + 1, p, j, memo))    # "*" matches >0 char
        elif p[j] == "?":
            isMatchBool = self.isMatchImpl(s, i + 1, p, j + 1, memo)
        else:
            if s[i] != p[j]: 
                isMatchBool = False
            else:
                isMatchBool = self.isMatchImpl(s, i + 1, p, j + 1, memo)
    
        memo[(i, j)] = isMatchBool  
        return isMatchBool