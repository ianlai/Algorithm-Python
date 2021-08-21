class Solution:
        
    # Backtracking + Memoization [Time O(n*2 + 2^n): 88% / Space: 88%]
    def partition(self, s: str) -> List[List[str]]:
        print("Backtracking(Index) + Memoization")
        if not s:
            return []
        
        #Prepare palindrome matrix
        self.palindromeMatrix = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.palindromeMatrix[i][j] = self.isPalindrome(s, i, j)
        
        #DFS (with memoization)
        results = [] 
        self.helper(s, 0, len(s)-1, [], results)
        return results
    
    def helper(self, s, left, right, cur, results):
        if left > right:
            return 
        
        if self.palindromeMatrix[left][right]:
            results.append(cur + [s[left:right+1]])
        
        for i in range(left, right):
            if self.palindromeMatrix[left][i]:
                self.helper(s, i+1, right, cur + [s[left:i+1]], results)
                
    def isPalindrome(self, s, i, j):
        return True if i > j or s[i] == s[j] and self.isPalindrome(s, i+1, j-1) else False 
    
    # =============================================
        
    # Backtracking [O(n*2^n): 51%]
    def partition2(self, s: str) -> List[List[str]]:
        print("Backtracking(Index)")
        if not s:
            return []
        
        #DFS
        results = [] 
        self.helper2(s, 0, len(s)-1, [], results)
        return results
    
    def helper2(self, s, left, right, cur, results):
        if left > right:
            return 
        
        if self.isPalindrome2(s, left, right):
            results.append(cur + [s[left:right+1]])
        
        for i in range(left, right):
            if self.isPalindrome2(s, left, i):
                self.helper2(s, i+1, right, cur + [s[left:i+1]], results)
                
    def isPalindrome2(self, s, i, j):
        return True if i > j or s[i] == s[j] and self.isPalindrome2(s, i+1, j-1) else False 
    
    # =============================================
    
    # Backtracking [O(n*2^n): 51%]
    def partition1(self, s: str) -> List[List[str]]:
        print("Backtracking(Slice)")
        if not s:
            return []
        
        results = []            
        self.helper1(s, [], results)
        return results
    
    def helper1(self, s, cur, results):
        if self.isPalindrome1(s):
            results.append(cur + [s])
        
        if len(s) == 1:
            return 
        
        for i in range(len(s)-1):
            if self.isPalindrome1(s[:i+1]):
                self.helper1(s[i+1:], cur + [s[:i+1]], results)
                
    def isPalindrome1(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True