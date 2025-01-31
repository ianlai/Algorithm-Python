# https://leetcode.com/problems/longest-string-chain/
 
class Solution:
    
    # Memoization [Time = O(N*L^2) : 12% (list) -> 40% (set)]
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        
        self.used = {}
        self.length = 0 
        self.words = set(words) 
        
        for s in self.words:
            if s in self.used:
                continue
            self.length = max(self.length, self.helper(s))
        return self.length
    
    def helper(self, s):
        if s not in self.words: #empty s included 
            return 0
        if s in self.used:
            return self.used[s]
        
        remaining = -float('inf')
        for i in range(len(s)):
            left  = s[:i]    
            right = s[i+1:] 
            remaining = max(remaining, 1 + self.helper(left + right)) 
        self.used[s] = remaining 
        return self.used[s] 