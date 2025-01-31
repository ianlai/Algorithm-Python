class Solution:
    
    # 2021/08/22
    # Backtracking + DP (table)
    # Precaculate palindrome matrix with length loop + Initialized matrix with 2 values   
    # [Time O(n*2 + 2^n): 96% / Space: 71%]
    def partition(self, s: str) -> List[List[str]]:
        print("Code5: Backtracking(Index) + Precaculate palindrome matrix with length loop + Initialized matrix with 2 values ")
        if not s:
            return []
        
        def isPalindrome(s, i, j):
            return True if s[i] == s[j] and self.palindromeMatrix[i+1][j-1] else False
        
        def helper(s, left, right, cur, results):
            if left > right:
                return 

            if self.palindromeMatrix[left][right]:
                results.append(cur + [s[left:right+1]])

            for i in range(left, right):
                if self.palindromeMatrix[left][i]: #left~i is palindrome
                    helper(s, i+1, right, cur + [s[left:i+1]], results) #further test for i+1~right
        
        #Precaculate palindrome matrix
        self.palindromeMatrix = [[True if i >= j else False for j in range(len(s))] for i in range(len(s))]
        for d in range(len(s)):
            for i in range(len(s)):
                j = i + d
                if j >= len(s):
                    break
                if (j-i) >= 1:   
                    self.palindromeMatrix[i][j] = isPalindrome(s, i, j)
                    
        #DFS (with memoization)
        results = [] 
        helper(s, 0, len(s)-1, [], results)
        return results
    
    # =============================================
    
    # Backtracking + Precaculate palindrome matrix with length loop [Time O(n*2 + 2^n): 96% / Space: 71%]
    def partition4(self, s: str) -> List[List[str]]:
        print("Code4: Backtracking(Index) + Precaculate palindrome matrix with length loop")
        if not s:
            return []
        
        #Precaculate palindrome matrix
        self.palindromeMatrix = [[False for j in range(len(s))] for i in range(len(s))]
        
        for d in range(len(s)):
            for i in range(len(s)):
                j = i + d
                if j >= len(s):
                    continue
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
        if (j - i) <= 0:
            return True
        if (j - i) == 1 and s[i] == s[j]:
            return True
        if (j - i) >= 2 and s[i] == s[j] and self.palindromeMatrix[i+1][j-1]:
            return True
        return False 
    
    # =============================================
        
    # Backtracking + Precaculate palindrome matrix  [Time O(n*3 + 2^n): 88% / Space: 88%]
    def partition3(self, s: str) -> List[List[str]]:
        print("Code3: Backtracking(Index) + Precaculate palindrome matrix")
        if not s:
            return []
        
        #Prepare palindrome matrix
        self.palindromeMatrix = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.palindromeMatrix[i][j] = self.isPalindrome3(s, i, j)
        
        #DFS (with memoization)
        results = [] 
        self.helper3(s, 0, len(s)-1, [], results)
        return results
    
    def helper3(self, s, left, right, cur, results):
        if left > right:
            return 
        
        if self.palindromeMatrix[left][right]:
            results.append(cur + [s[left:right+1]])
        
        for i in range(left, right):
            if self.palindromeMatrix[left][i]:
                self.helper3(s, i+1, right, cur + [s[left:i+1]], results)
                
    def isPalindrome3(self, s, i, j):
        return True if i > j or s[i] == s[j] and self.isPalindrome3(s, i+1, j-1) else False 
    
    # =============================================
        
    # Backtracking [O(n*2^n): 51%]
    def partition2(self, s: str) -> List[List[str]]:
        print("Code2: Backtracking(Index)")
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
        print("Code1: Backtracking(Slice)")
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