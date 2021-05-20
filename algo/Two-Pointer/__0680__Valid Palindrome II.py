class Solution:
    # Two-Pointer, remove left or right when facing difference, passing index [O(n), 51%]
    def validPalindrome(self, s: str) -> bool:
        print("Method-0")
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
        
    def isPalindrome(self, s: str, left, right) -> bool:
        if not s:
            return True
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # ==============================================
    
    # Two-Pointer, remove left or right when facing difference, using slicing [O(n), 9%]
    def validPalindrome1(self, s: str) -> bool:
        print("Method-1")
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            # while left < right and not s[left].isalpha() and not s[left].isdigit():
            #     left += 1
            # while left < right and not s[right].isalpha() and not s[right].isdigit():
            #     right -= 1
            if s[left].lower() != s[right].lower():
                return self.isPalindrome1(s[left+1:right+1]) or self.isPalindrome1(s[left:right])
            left += 1
            right -= 1
        return True
        
    def isPalindrome1(self, s: str) -> bool:
        #print(s)
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            #print(s[left], s[right])
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            