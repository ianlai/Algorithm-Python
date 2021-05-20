class Solution:
    
    # Two-Pointer [O(n), 39%]
    def isPalindrome(self, s: str) -> bool:
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
            