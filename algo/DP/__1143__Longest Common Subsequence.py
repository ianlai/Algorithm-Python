class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        memo = {}
        return self.helper(text1, text2, 0, 0, memo)
        #return self.helper1(text1, text2, memo)
        
    def helper(self, text1, text2, p1, p2, memo):
        if (p1, p2) in memo:
            return memo[(p1, p2)]   
        
        if p1 >= len(text1) or p2 >= len(text2):
            return 0
        
        count = 0
        try:
            idx2 = text2.index(text1[p1], p2)
        except ValueError:
            count = self.helper(text1, text2, p1+1, p2, memo)
            memo[(p1, p2)] = count
            return count 
    
        a = self.helper(text1, text2, p1+1, idx2+1, memo) + 1
        b = self.helper(text1, text2, p1+1, p2, memo)
        
        count = max(a, b) 
        memo[(p1, p2)] = count
        return count 
            
        
        
        
        
    
    def helper1(self, text1, text2, memo):
        if not text1 or not text2:
            return 0
        
        if (text1, text2) in memo:
            return memo[(text1, text2)]  
        
        count = 0
        try:
            idx2 = text2.index(text1[0])
        except ValueError:
            count = self.helper1(text1[1:], text2, memo)
            memo[(text1, text2)] = count
            return count 
    
        a = self.helper1(text1[1:], text2[idx2+1:], memo) + 1
        b = self.helper1(text1[1:], text2, memo)
        
        # if a >= b:
        #     print("a >= b")
        # else:
        #     print("a <  b")
        # print("  ", a, text1[1:], text2[idx2+1:])
        # print("  ", b, text1[1:], text2)
        
        count = max(a, b) 
        memo[(text1, text2)] = count
        return count 