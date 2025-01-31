class Solution:
    
    # Top-down DP [O(L3), 5%]   //len(s): L, len(wordDict): n
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
        
        wordSet = set(wordDict)
        memo = {}
        return self.checkSeparatible(s, 0, len(s), wordSet, memo)
    
    def checkSeparatible(self, s, i, j, wordSet, memo):
        if i >= j:
            return True
        if (i, j) in memo:
            return memo[(i, j)]
        if s[i:j] in wordSet:
            return True
        
        for k in range(i + 1, j):
            if not self.checkSeparatible(s, i, k, wordSet, memo):
                continue
            if not self.checkSeparatible(s, k, j, wordSet, memo):
                continue
            memo[(i, j)] = True
            return True  
            
        memo[(i, j)] = False
        return False 
    
    
#     # DFS [TLE]
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         if not s:
#             return True
#         if not wordDict:
#             return False
        
#         wordSet = set(wordDict)
#         #print(wordSet)
    
#         return self.checkSeparatible(s, wordSet)
    
#     def checkSeparatible(self, s, wordSet):
#         if not s:
#             return True
#         #print(s)
#         if s in wordSet:
#             #print(">>", s)
#             return True
        
#         for i in range(1, len(s)):
#             if self.checkSeparatible(s[:i], wordSet) and self.checkSeparatible(s[i:], wordSet):
#                 return True
#         return False 