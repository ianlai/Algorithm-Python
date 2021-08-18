class Solution:
    
    # Backtracking [O(n*2^n): 51%]
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        results = []            
        self.helper(s, [], results)
        return results
    
    def helper(self, s, cur, results):
        if self.isPalindrome(s):
            results.append(cur + [s])
            
        if len(s) == 1:
            return 
        
        for i in range(len(s)-1):
            if self.isPalindrome(s[:i+1]):
                self.helper(s[i+1:], cur + [s[:i+1]], results)
                
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True