class Solution:
    
    # Memoization DP [O(2^(m+n) --> O(m*n), 80%]
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.isMatchImpl(s, 0, p, 0, memo)
    
    def isMatchImpl(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        #print(i, j)
        
        if i == len(s) and j == len(p):
            memo[(i, j)] = True
            return True
        elif i != len(s) and j == len(p):
            memo[(i, j)] = False
            return False
        elif i == len(s) and j != len(p):
            leftoverLen = len(p) - j
            if leftoverLen % 2 == 1:  #leftover number is odd
                return False
            for k in range(leftoverLen):
                idx = j + k
                if k % 2 == 1 and p[idx] != "*": #all "j + odd" p[] need to be "*" otherwise False (e.g. j+1, j+3)
                    memo[(i, j)] = False
                    return False
            memo[(i, j)] = True
            return True
        
        
        isMatchBool = None 
        if j + 1 < len(p) and p[j + 1] == "*": 
            if p[j] == s[i] or p[j] == ".": 
                isMatchBool = self.isMatchImpl(s, i + 1, p, j, memo) 
            isMatchBool = self.isMatchImpl(s, i, p, j + 2, memo) or isMatchBool
        else:    
            if p[j] == ".":
                isMatchBool = self.isMatchImpl(s, i + 1, p, j + 1, memo)
            else: 
                if s[i] != p[j]:
                    memo[(i, j)] = False
                    return False
                isMatchBool = self.isMatchImpl(s, i + 1, p, j + 1, memo) 
        memo[(i, j)] = isMatchBool
        return isMatchBool